from pathlib import Path
import pandas as pd


class CsvIngest:
    """
    The CsvIngest class opens a .csv file and
    parses it into dictionaries which can later be serialized to JSON for
    upload to the catalyst properties database (CPD) API.
    """

    def __init__(self, csv_filename: str):
        """
        __init__ creates instance attributes used for parsing the .csv
        file.

        Parameters
        ----------
        csv_filename: str
            Absolute path to .csv file to ingest.

        Raises
        ------
        CsvIngestException
            Raises an exception if the filename does not exist.
        """
        test_csv_path = Path(csv_filename)
        if not test_csv_path.is_file():
            raise CsvIngestException(f"Could not find input .csv file {csv_filename}")
        self.csv_filename = csv_filename


class CsvIngestException(Exception):
    """
    CsvIngestException is a custm exception class for errors that occur during
    the csv ingestion process. A custom Exception class allows fine-grained
    exception handling and better error messages for users.
    """

    def __init__(self, message: str):
        """
        __init__ calls the superclass __init__ to set up the custom message for
        this CsvIngestException.

        Parameters
        ----------
        message : str
            A message for the user.
        """
        super(CsvIngestException, self).__init__(message)
