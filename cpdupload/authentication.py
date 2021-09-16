import logging
import getpass
import boto3


class Authentication:
    def __init__(self, client_id, username):
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.username = username
        self.password = None

    def prompt_password(self):
        self.password = getpass.getpass()

    def authenticate_and_get_token(self):
        client = boto3.client('cognito-idp')

        try:
            resp = client.initiate_auth(
                ClientId=self.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": self.username,
                    "PASSWORD": self.password
                }
            )
        except Exception as e:
            raise AuthenticationException(f"User authentication failed. {e}")

        self.logger.info(f"Authentication for user {self.username} was successful.")
        return resp['AuthenticationResult']['AccessToken']


class AuthenticationException(Exception):
    def __init__(self, message):
        super(AuthenticationException, self).__init__(message)
