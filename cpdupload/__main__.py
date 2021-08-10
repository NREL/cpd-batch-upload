"""
The __main__ modules is a basic implementation of a command prompt interface to upload CPD
data.
"""

import argparse
from cpdupload.loader import Loader, LoaderException


try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="file to import, .csv or .json format")
    parser.add_argument("--api", help="URL to API.")
    args = parser.parse_args()
    loader = Loader(input_filename=args.input, api=args.api)
    loader.send_adsorption_measurement_to_api()
    print("Successfully loaded adsorption measurement(s) to the API.")
except LoaderException as e:
    print(e)
