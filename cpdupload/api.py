import json
import logging
from typing import Dict, Any, List
from requests import get, post, codes, RequestException  # type: ignore


class API:
    """
    The API class contains the logic to connect to the CPD API.
    """

    def __init__(self, url: str, token: str):
        """
        Parameters
        ----------
        url: str
            The base URL of the API.

        token: str
            Bearer token to use for authentication.
        """
        self.url = url
        self.token = token
        self.logger = logging.getLogger(__name__)

    def health_check(self) -> int:
        """
        health_check connects to the health_check API. It returns the response
        code if the request succeeds and raises an exception if the connection
        fails.

        Returns
        -------
        int
            Returns the response status code.

        Raises
        ------
        APIException
            Raises an API exception if a non-200 exception is raised or the connection
            fails for any reason.
        """
        request_url = f"{self.url}"
        try:
            response = get(request_url)
            self.logger.info(f"Health check request to {request_url} succeeded.")
            if response.status_code != codes.ok:
                raise APIException(
                    f"API health check failed. Received status code {response.status_code}"
                )
            return response.status_code
        except RequestException as e:
            raise APIException(
                f"API Health check failed. Could not connect to {request_url}"
            )

    def adsorption_measurement_load(self, payload: List[Dict[str, Any]]) -> int:
        """
        adsorption_measurement_load() attempts to load a JSON payload of an adsorption
        measurement into the API.

        Parameters
        ----------
        payload: Dict[str, Any]
            The nested dictionary structure from which to create JSON.

        Returns
        -------
        int
            The status code of the successful request.

        Raises
        ------
        APIException
            Raises an API exception if any errors happen in the request or on the API.
        """
        request_url = f"{self.url}/adsorption_measurement/load"
        json_payload = json.dumps(payload)
        try:
            self.logger.info(f"Attempting to post JSON to {request_url}.")
            headers = {"Authorization": f"Bearer {self.token}"}
            response = post(request_url, data=json_payload, headers=headers)
            self.logger.info(
                f"Posting JSON to API at {request_url} resulted in status code {response.status_code}."
            )
            if response.status_code != codes.ok:
                raise APIException(
                    f"adsorption_measurement/load failed with status {response.status_code} and response {response.text}"
                )
            return response.status_code
        except RequestException as err:
            raise APIException(f"adsorption_measurement/load failed because: {err}")


class APIException(Exception):
    """
    APIException is a custom exception class for errors that occur during
    the API connection process. A custom Exception class allows fine-grained
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
        super(APIException, self).__init__(message)
