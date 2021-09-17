import logging
import getpass
import os

from warrant import AWSSRP
import boto3


class Authentication:
    def __init__(self, client_id: str, pool_id: str, username: str):
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.pool_id = pool_id
        self.username = username
        self.password = None

    def prompt_password(self):
        self.password = getpass.getpass()

    def authenticate_and_get_token(self) -> str:
        self.logger.info(f"Pool: {self.pool_id} client: {self.client_id} user: {self.username}")
        client = boto3.client('cognito-idp')
        aws = AWSSRP(username=self.username, password=self.password, pool_id=self.pool_id,
                     client_id=self.client_id, client=client)
        tokens = aws.authenticate_user()
        return tokens


class AuthenticationException(Exception):
    def __init__(self, message):
        super(AuthenticationException, self).__init__(message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client_id = os.environ.get("COGNITO_CLIENT_ID", "")
    pool_id = os.environ.get("COGNITO_POOL_ID", "")
    username = os.environ.get("COGNITO_USERNAME", "")
    auth = Authentication(client_id, pool_id, username)
    auth.prompt_password()
    tokens = auth.authenticate_and_get_token()
    print(tokens)
