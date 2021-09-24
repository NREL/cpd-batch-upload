"""
The __main__ modules is a basic implementation of a command prompt interface to upload CPD
data.
"""

import argparse
import logging
import yaml  # type: ignore
from cpdupload.loader import Loader, LoaderException
from cpdupload.authentication import Authentication, AuthenticationException

logger = logging.getLogger(__name__)

try:
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", help="file to import, .csv or .json format", required=True
    )
    parser.add_argument(
        "--verbose",
        help="If specified, script will display verbose output during operation.",
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument("--config", help="Config for API connectivity", required=True)
    parser.add_argument("--username", help="Username for authentication", required=True)
    args = parser.parse_args()

    # Parse the config file with some defaults.
    with open(args.config, "r") as f:
        config = yaml.load(f, yaml.FullLoader)
    cognito = config.get("cognito", {})
    api = config.get("api", {})
    host_url = api.get("host_url", "")
    cognito_pool_id = cognito.get("pool_id", "")
    cognito_client_id = cognito.get("client_id")

    # If verbose option is specified, show verbose logging.
    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    # Setup authentication
    auth = Authentication(cognito_client_id, cognito_pool_id, args.username)
    auth.prompt_password()
    token = auth.authenticate_and_get_token()

    # Create a loader which wraps file reading, parsing, and API connection functionality
    loader = Loader(input_filename=args.input, api=host_url, token=token)

    # Send the parsed file to the API
    loader.send_adsorption_measurement_to_api()

    # Report a success message to the user
    print("Successfully loaded adsorption measurement(s) to the API.")

# Print any errors that happen in a user-friendly format
except LoaderException as e:
    print(e)
    exit(1)
except AuthenticationException as e:
    print(e)
    exit(2)
