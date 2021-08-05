"""
This is a basic implementation of a command prompt interface to upload CPD
data.
"""
import json
from typing import Dict, Any, List, Union
import argparse

from cpdupload.csvingest import CsvIngest, CsvIngestException
from cpdupload.jsonbuilder import JSONBuilder, JSONBuilderException
from cpdupload.api import API, APIException


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="csv file to import")
    parser.add_argument("--api", help="URL to API.")
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_arguments()
    try:
        api = API(args.api)
        api.health_check()
        print("API health check successful...")
        ingest = CsvIngest(args.csv)
        print("csv parse successful...")
        rows: List[Dict[str, Union[int, str, float]]] = ingest.load_csv()
        builder = JSONBuilder()
        top_json = builder.parse_rows(rows)
        print("JSON build successful...")
        api.adsorption_measurement_load(top_json)
        with open("output.json", "w") as file:
            file.write(json.dumps(top_json))
    except CsvIngestException as err:
        print(f"Error while parsing csv file: {err}")
    except JSONBuilderException as err:
        print(f"Error while building the JSON: {err}")
    except APIException as err:
        print(f"Error connecting to the CKAN API: {err}")


if __name__ == "__main__":
    main()
