"""
This is a basic implementation of a command prompt interface to upload CPD
data.
"""

from typing import Dict, Any, List, Union
from cpdupload.csvingest import CsvIngest, CsvIngestException
import argparse
import json


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="csv file to import")
    args = parser.parse_args()
    return args


def store_key(d: Dict, key_path: list, value: Any):
    head = key_path[0]
    tail = key_path[1:]

    if len(tail) > 0 and head not in d:
        d[head] = {}
        store_key(d[head], tail, value)
    elif len(tail) > 0 and head in d:
        store_key(d[head], tail, value)
    else:
        d[head] = value


def parse_ints_out_of_key_path(key_path: List[str]) -> List[Union[str, int]]:
    result: List[Union[str, int]] = []
    for key in key_path:
        if is_int(key):
            result.append(int(key))
        else:
            result.append(key)
    return result


def is_int(value: Any) -> bool:
    try:
        int(value)
        return True
    except ValueError as e:
        return False


def main() -> None:
    args = parse_arguments()
    print(f"Attempting to parse {args.csv}")
    try:
        ingest = CsvIngest(args.csv)
        rows = ingest.load_csv()
        for row in rows:
            top_dict = {}
            for key, value in row.items():
                key_path = key.split(".")
                store_key(top_dict, key_path, value)
            top_json = json.dumps(top_dict)
            print(top_json)
    except CsvIngestException as err:
        print(err)


if __name__ == "__main__":
    main()
