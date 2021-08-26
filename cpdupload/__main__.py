"""
The __main__ modules is a basic implementation of a command prompt interface to upload CPD
data.
"""

import argparse
import logging
from cpdupload.loader import Loader, LoaderException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="file to import, .csv or .json format")
    parser.add_argument("--api", help="URL to API.")
    args = parser.parse_args()

    # Create a loader which wraps file reading, parsing, and API connection functionality
    loader = Loader(input_filename=args.input, api=args.api)

    # Send the parsed file to the API
    loader.send_adsorption_measurement_to_api()

    # Report a success message to the user
    print("Successfully loaded adsorption measurement(s) to the API.")

# Print any errors that happen in a user-friendly format
except LoaderException as e:
    print(e)
