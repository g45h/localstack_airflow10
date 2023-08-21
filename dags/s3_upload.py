import os
import boto3
from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

S3_BUCKET_NAME = 'task10'
local_folder_path = './data/'
file_list = os.listdir(local_folder_path)
result_list = list(map(lambda s: local_folder_path + s, file_list))

# AWS S3 credentials
AWS_S3_CREDS = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "aws_session_token": os.getenv("AWS_SESSION_TOKEN"),
    "endpoint_url": "http://1d7eb4b09922:4566/"
}
s3 = boto3.client('s3', **AWS_S3_CREDS)

args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 31),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='s3_upload',
    default_args=args,
    schedule_interval=None,
) as dag:
    @task
    def upload_to_bucker(filename: str):
        filename = '/data/2019_10.csv'
        print(f"[INFO] Uploading {filename} to S3 bucket")
        response = s3.list_buckets()
        print('Regions:', response)
        # s3.upload_file(Filename=filename, Bucket=S3_BUCKET_NAME, Key=os.getenv("AWS_SECRET_ACCESS_KEY"))
        return filename

    first = upload_to_bucker.expand(filename=result_list)
   