"""
This is a basic implementation of a command prompt interface to upload CPD
data.
"""

from cpdupload.csvingest import CsvIngest, CsvIngestException
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="csv file to import")
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_arguments()
    print(f"Attempting to parse {args.csv}")
    try:
        ingest = CsvIngest(args.csv)
        rows = ingest.load_csv()
        print("stop here")
    except CsvIngestException as err:
        print(err)


if __name__ == "__main__":
    main()
