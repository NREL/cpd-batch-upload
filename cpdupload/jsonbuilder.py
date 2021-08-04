from typing import List, Dict, Union, Any


class JSONBuilder:
    """
    JSONBuilder takes a list of rows and creates a graph of JSON to send to the
    CPD API.
    """

    def parse_rows(
        self, csv_rows: List[Dict[str, Union[str, float, int]]]
    ) -> List[Dict[str, Any]]:
        """
        parse_rows() parses rows read by a CsvIngest instance. It creates the structure
        of dictionaries and list nested in dictionaries and lists for upload to the
        CPD API.

        Parameters
        ----------
        csv_rows: List[Dict[str, Union[str, float, int]]]
            Rows as parsed out of the csv file. See the load_csv() method in the CsvIngest
            class for the format of the rows. Each dictionary is a single level of key/value
            pairs, with the keys being column names and the values being str, float, or int.

        Returns
        -------
        List[Dict[str, Any]]
            Returns a list of nested dictionaries suitable for conversion to JSON.
        """
        json_rows: List[Dict[str, Any]] = []
        for idx, row in enumerate(csv_rows):
            json_row: Dict[str, Any] = {}
            for key, value in row.items():
                key_path = self.parse_ints_out_of_key_path(key.split("."))
                self.store_key(json_row, key_path, value, idx)
            json_rows.append(json_row)
        return json_rows

    def store_key(
        self,
        d: Union[Dict, List],
        key_path: List[Any],
        value: Any,
        idx: int,
    ) -> None:
        """
        store_key() recursively sets key/value pairs on nested dictionaries and lists of
        dictionaries based on the flattened key value pairs in d. For example, if d
        contained:

        {"one.two.three": 4}

        This method would return:

        {"one": {"two": {"three": 4}}}

        Parameters
        ----------
        d: Union[Dict, List]
            d is either a list or a dictionary into which to insert the value or recursively
            create another list or dictionary.

        key_path: List[Union[str, int]]
            The sequence of keys under which to store the value. If an element is a string,
            the next recursive level will be a dictionary. If the element is any integer,
            the next recursive level is a list. Note: this method looks to the data type
            as the hint about what to do; a string of "1" will store a dictionary key of "1"
            not start a new list.

        value: Any
            The value to be stored at the end of the key path.

        idx: int
            This should be passed into the first call of this method. It is not changed on
            subsequent recursions. It is used when an exception needs to be raised to
            report the row of the spreadsheet on which the error was found.

        Returns
        -------
        None
            This method does not return a value because d is mutated in place.

        Raises
        ------
        JSONBuilderException
            Raises a JSONBuilderException if a duplicate column name is found.
        """

        if len(key_path) < 1:
            raise JSONBuilderException(
                f"Duplicate column found on row {idx + 2} of csv. Value: {value}"
            )

        head = key_path[0]
        tail = key_path[1:]

        if len(tail) > 0:
            if type(tail[0]) == int and head not in d:
                d[head] = [{}]
                self.store_key(d[head][-1], tail[1:], value, idx)
            elif type(tail[0]) == int and head in d:
                if len(d[head]) == tail[0] + 1:
                    self.store_key(d[head][-1], tail[1:], value, idx)
                else:
                    d[head].append({})
                    self.store_key(d[head][-1], tail[1:], value, idx)
            elif type(tail[0]) == str and head not in d:
                d[head] = {}
                self.store_key(d[head], tail, value, idx)
            else:
                self.store_key(d[head], tail, value, idx)
        else:
            d[head] = value

    def parse_ints_out_of_key_path(self, key_path: List[str]) -> List[Union[str, int]]:
        """
        parse_ints_out_of_key_path() parses a list of strings into a list of strings and
        integers. This allows the store_key() method to nest lists inside dictionaries.

        Parameters
        ----------
        key_path: List[str]
            The list of keys for nested dictionaries.

        Returns
        -------
        List[Union[str, int]]
            A list of strings and integers to navigate a nested dictionary structure.
        """
        result: List[Union[str, int]] = []
        for key in key_path:
            if self.is_int(key):
                result.append(int(key))
            else:
                result.append(key)
        return result

    @staticmethod
    def is_int(value: Any) -> bool:
        """
        is_int returns True or False depending on whether the value passed to it
        can be parsed as an integer.

        Parameters
        ----------
        value: Any
            The value under test.

        Returns
        -------
        bool
            True if the value can be parsed as an integer, False otherwise.
        """
        try:
            int(value)
            return True
        except ValueError as e:
            return False


class JSONBuilderException(Exception):
    """
    JSONBuilderException is a custom exception class for errors that occur during
    the JSON building process. A custom Exception class allows fine-grained
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
        super(JSONBuilderException, self).__init__(message)
