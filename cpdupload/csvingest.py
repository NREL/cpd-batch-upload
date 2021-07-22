from typing import Dict, List, Union, Any
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
        csv_filename : str
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

    def load_csv(self) -> List[Dict[str, Union[int, float, str, bool]]]:
        """
        load_csv() loads the dataframe, iterates over each row, and creates a list
        of dictionaries that can then be further processed into nested dictionaries
        to upload to the api. Integer and float columns are parsed by Pandas as the
        dataframe is loaded. "TRUE" or "FALSE" values are parsed by the is_true_false()
        method below.

        This method returns a list of dictionaries. Each dictionary has a single level
        of key/value pairs corresponding to the column. There is one dictionary per
        row stored in the list. If a particular column in a row is empty (a Pandas nan)
        then no key/value pair is in that row for that key.

        Returns
        -------
        List[Dict[str, Union[int, float, str, bool]]]
            The list of dictionaries as described above.
        """
        df = pd.read_csv(self.csv_filename)
        result = []
        for _, row in df.iterrows():
            parsed_row = {}
            for col, value in row.iteritems():
                if not pd.isnull(value):
                    is_true_false = self.is_true_false(value)
                    parsed_row[col] = (
                        is_true_false["value"]
                        if is_true_false["is_true_false"]
                        else value
                    )
            result.append(parsed_row)
        return result

    @staticmethod
    def is_true_false(value: Any) -> Dict[str, bool]:
        """
        is_true_false() looks at the given value to determine if it is
        either of the strings "TRUE" or "FALSE". It returns the result of
        this parse attempt in a dictionary. The dictionary will have two keys
        in it:

        result["is_true_false"]: True if the string is either "TRUE" or "FALSE"

        result["value"]: If "is_true_or_false" key is True, then this key is True
        or False to correspond to the original value.

        Parameters
        ----------
        value: Any
            A value to evaluate.

        Returns
        -------
        Dict[str, bool]
            A dictionary as described above.
        """
        result_is_not_true_false = {"is_true_false": False, "value": False}

        if type(value) == str:
            test_value = value.upper()
            if test_value == "TRUE" or test_value == "FALSE":
                return {"is_true_false": True, "value": test_value == "TRUE"}
            else:
                return result_is_not_true_false
        else:
            return result_is_not_true_false


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
