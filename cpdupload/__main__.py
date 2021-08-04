"""
This is a basic implementation of a command prompt interface to upload CPD
data.
"""
import json
from typing import Dict, Any, List, Union
from cpdupload.csvingest import CsvIngest, CsvIngestException
from cpdupload.jsonbuilder import JSONBuilder, JSONBuilderException
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="csv file to import")
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_arguments()
    try:
        ingest = CsvIngest(args.csv)
        rows: List[Dict[str, Union[int, str, float]]] = ingest.load_csv()
        builder = JSONBuilder()
        top_json = builder.parse_rows(rows)
        with open('output.json', 'w') as file:
            file.write(json.dumps(top_json))
    except CsvIngestException as err:
        print(err)


if __name__ == "__main__":
    main()
