import os
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import boto3

S3_BUCKET_NAME = 'task10'

local_folder_path = './data/'
file_list = os.listdir(local_folder_path)
result_list = list(map(lambda s: local_folder_path + s, file_list))
counter = 0

# AWS S3 credentials
AWS_S3_CREDS = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "aws_session_token": os.getenv("AWS_SESSION_TOKEN"),
    "endpoint_url": "http://localhost:4566/"
}


def upload_file_to_s3(x: int):
    # s3 = boto3.client('s3', **AWS_S3_CREDS)
    # global counter
    # # filename = result_list[counter]
    # file = fileslist[counter]
    # print(f"[INFO] Uploading {file} to S3 bucket")
    # s3.upload_file(Filename=file, Bucket=S3_BUCKET_NAME, Key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    # counter = counter + 1
    print(x)
    return x


args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 31),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
}

with DAG(
    dag_id='shto',
    default_args=args,
    schedule_interval=None,
) as dag:
    to_s3 = PythonOperator.partial(
        task_id='upload_file_to_s3',
        python_callable=upload_file_to_s3,
    ).expand(x=[1, 2, 3])
