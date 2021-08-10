import os
import json
from typing import Dict, List, Union

from cpdupload.csvingest import CsvIngest, CsvIngestException
from cpdupload.jsonbuilder import JSONBuilder, JSONBuilderException
from cpdupload.api import API, APIException


class Loader:
    """
    The Loader class unifies the API load workflow. It has a method to accept a filename
    and attempt to upload it to the API.
    """

    def __init__(self, input_filename: str, api: str):
        """
        This constructor accepts an input filename as a parameter and checks to
        ensure the filename exists before any load operation happens.

        Parameters
        ----------
        input_filename: str
            The input filename for the load operation.

        api: str
            The base URL of the CPD API server.

        Raises
        ------
        LoaderException
            Raises a LoaderException if the filename is not found or the API health check
            endpoint cannot be contacted.
        """
        if not os.path.isfile(input_filename):
            raise LoaderException(
                f"Cannot import {input_filename} because the file was not found."
            )

        self.input_filename = input_filename

        try:
            api_check = API(api)
            api_check.health_check()
            self.api = api
        except APIException as e:
            raise LoaderException(str(e))

    def send_adsorption_measurement_to_api(self):
        """
        send_file_to_api loads the file given, checks to see if it
        is JSON or CSV, parses a CSV if necessary, and then sends the JSON payload
        to the API.

        Raises
        ------
        LoaderException
            Raises an exception if something goes wrong with the file parsing or
            upload to the API.
        """
        try:
            api = API(self.api)
            
            if self.input_filename.endswith(".csv"):
                ingest = CsvIngest(self.input_filename)
                rows: List[Dict[str, Union[int, str, float]]] = ingest.load_csv()
                builder = JSONBuilder()
                json_for_upload = builder.parse_rows(rows)
            else:
                with open(self.input_filename, "r") as file:
                    json_for_upload = json.loads(file.read())

            api.adsorption_measurement_load(json_for_upload)

        except CsvIngestException as err:
            raise LoaderException(f"Error while parsing CSV file: {err}")
        except JSONBuilderException as err:
            raise LoaderException(f"Error while building the JSON: {err}")
        except APIException as err:
            raise LoaderException(f"Error connecting to the CKAN API: {err}")


class LoaderException(Exception):
    """
    The LoaderException class is for exceptions raised during a load operation. It is
    raised as part of the exception handling of the Loader class. Use of this exception
    generally follows a two step process:

    1. A JSONBuilderException, CsvIngestException, or APIException is caught by an
    instance of the Loader class.

    2. That original exception is reported to the user with a print statement.

    3. A loader exception is raised that contains the original message as well as
    any additional context information of for the Loader exception.

    4. The code calling the instance of this Loader class can then catch the
    LoaderException and report it to the user.

    Additionally, a LoaderException can be raised on its own by the Loader class
    for errors that fall outside the scope of the other three exceptions.

    For the message in the exception, emphasis should be placed on an error message
    that can be shown to a user with some actionable meaning.
    """

    def __init__(self, message: str):
        """
        Accepts a message that should be descriptive for display to a user.

        Parameters
        ----------
        message: str
            An error message useful to an end user.
        """
        super(LoaderException, self).__init__(message)
