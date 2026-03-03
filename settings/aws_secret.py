import boto3
import json
import os
from botocore.exceptions import ClientError

class AwsSecretManager:
    def __init__(self):
        self.client = boto3.client(
            "secretsmanager",
            region_name=os.getenv("AWS_REGION")
        )

    def get_secret(self, secret_name):
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            return json.loads(response["SecretString"])
        except ClientError as e:
            raise Exception(f"Error obteniendo secreto: {e}")