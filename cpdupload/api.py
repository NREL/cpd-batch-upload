from requests import get, post, codes, RequestException


class API:
    """
    The API class contains the logic to connect to the CPD API.
    """

    def __init__(self, url: str):
        """
        Parameters
        ----------
        url: str
            The base URL of the API.
        """
        self.url = url

    def health_check(self) -> str:
        """
        health_check connects to the health_check API. It returns the response
        code if the request succeeds and raises an exception if the connection
        fails.

        Returns
        -------
        str
            Returns the response body if the health check is successful

        Raises
        ------
        APIException
            Raises an API exception if a non-200 exception is raised or the connection
            fails for any reason.
        """
        request_url = f"{self.url}"
        try:
            response = get(request_url)
            if response.status_code != codes.ok:
                raise APIException(f"Health check failed. Received status code {response.status_code}")
            return response.text
        except RequestException as e:
            raise APIException(f"Health check failed. Could not connect to {request_url}")


class APIException(Exception):
    """
    APIException is a custom exception class for errors that occur during
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
        super(APIException, self).__init__(message)
