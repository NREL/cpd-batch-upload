from typing import List, Dict, Union, Any


class JSONBuilder:
    """
    JSONBuilder takes a list of rows and creates a graph of JSON to send to the
    CPD API.
    """

    def parse_rows(self, csv_rows: List[Dict[str, Union[str, float, int]]]) -> List[Dict[str, Any]]:
        json_rows: List[Dict[str, Any]] = []
        for idx, row in enumerate(csv_rows):
            json_row: Dict[str, Any] = {}
            for key, value in row.items():
                key_path = self.parse_ints_out_of_key_path(key.split("."))
                self.store_key(json_row, key_path, value, idx)
            json_rows.append(json_row)
        return json_rows

    def store_key(self, d: Union[Dict, List], key_path: list, value: Any, idx: int):
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
        result: List[Union[str, int]] = []
        for key in key_path:
            if self.is_int(key):
                result.append(int(key))
            else:
                result.append(key)
        return result

    @staticmethod
    def is_int(value: Any) -> bool:
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
