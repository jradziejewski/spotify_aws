import boto3
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION


def connect_to_s3():
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )
        print("Connected to s3 successfully")
        return s3_client
    except Exception as e:
        print(e)


def upload_to_s3(s3_client, file_path: str, bucket_name: str, s3_file_name: str):
    try:
        print("Uploading file to s3 bucket " + bucket_name)
        print(file_path)
        s3_client.upload_file(file_path, bucket_name, s3_file_name)
        print("File uploaded to s3")
    except FileNotFoundError:
        print("File not found")
