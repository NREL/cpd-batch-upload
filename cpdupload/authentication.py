import boto3
import os


class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client_id = os.environ.get("COGNITO_CLIENT_ID", "")

    def authenticate_and_get_token(self):
        client = boto3.client('cognito-idp')

        resp = client.initiate_auth(
            ClientId=self.client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": self.username,
                "PASSWORD": self.password
            }
        )

        return resp['AuthenticationResult']['AccessToken']


if __name__ == "__main__":
    auth = Authentication(
        os.environ.get("COGNITO_USERNAME", "no username provided"),
        os.environ.get("COGNITO_PASSWORD", "no password provided")
    )
    print(auth.authenticate_and_get_token())
