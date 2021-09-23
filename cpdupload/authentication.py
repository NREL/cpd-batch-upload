import logging
import getpass

from warrant import AWSSRP
import boto3


class Authentication:
    """
    The Authentication class implements SRP authentication to AWS to access the CPD API
    """

    def __init__(self, client_id: str, pool_id: str, username: str):
        """
        Parameters
        ----------
        client_id: str
            The Cognito client id for the application.

        pool_id: str
            The Cognito pool id.

        username: str
            The username to attempt to authenticate.
        """
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.pool_id = pool_id
        self.username = username
        self.password = None

    def prompt_password(self):
        """
        prompt_password() securely retrieves the password from the user without
        echoing it while they are typing.
        """
        self.password = getpass.getpass()

    def authenticate_and_get_token(self) -> str:
        """
        Returns
        -------
        str
            The bearer token to use in an Authorization header.

        Raises
        ------
        AuthenticationException
            Raises an exception if the authentication fails.
        """
        self.logger.info(
            f"Pool: {self.pool_id} client: {self.client_id} user: {self.username}"
        )
        client = boto3.client("cognito-idp")

        try:
            aws = AWSSRP(
                username=self.username,
                password=self.password,
                pool_id=self.pool_id,
                client_id=self.client_id,
                client=client,
            )
            tokens = aws.authenticate_user()
            access_token = tokens["AuthenticationResult"]["IdToken"]
            return access_token
        except Exception as err:
            raise AuthenticationException(f"Could not authenticate user because: {err}")


class AuthenticationException(Exception):
    """
    AuthenticationException is a custom exception for authentication errors.
    """

    def __init__(self, message):
        super(AuthenticationException, self).__init__(message)
