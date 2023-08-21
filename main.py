import pandas as pd
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

def split_by_date(filepath):
    df = pd.read_csv(filepath)
    df['departure'] = pd.to_datetime(df['departure'])
    df['Year'], df['Month'] = df['departure'].dt.year, df['departure'].dt.month

    g = df.groupby(['Year', 'Month'])

    for name, group in g:
        group.to_csv(f"/home/user/PycharmProjects/localstack10/data/{name[0]}_{name[1]}.csv", index=False)


if __name__ == '__main__':
    # path = 'database.csv'
    # # split_by_date(path)
    #
    # AWS_S3_CREDS = {
    #     "aws_access_key_id": "test",  # os.getenv("AWS_ACCESS_KEY")
    #     "aws_secret_access_key": "test",  # os.getenv("AWS_SECRET_KEY")
    #     "aws_session_token": "test",
    #     "endpoint_url": "http://localhost:4566/"
    # }
    # s3 = boto3.client('s3', **AWS_S3_CREDS)
    # print("[INFO:] Connecting to cloud")
    #
    # # Retrieves all regions/endpoints that work with S3
    #
    S3_BUCKET_NAME = 'task10'
    # local_folder_path = './data/'
    # file_list = os.listdir(local_folder_path)
    # result_list = list(map(lambda s: local_folder_path + s, file_list))

    # AWS S3 credentials
    AWS_S3_CREDS = {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "aws_session_token": os.getenv("AWS_SESSION_TOKEN"),
        "endpoint_url": "http://localhost:4566/"
    }
   #  test = os.getenv("KEY")
    s3 = boto3.client('s3', **AWS_S3_CREDS)
    filename = '/data/2019_10.csv'
    print(f"[INFO] Uploading {filename} to S3 bucket")

    # response = s3.list_buckets()
    # print('Regions:', response)
    s3.upload_file(Filename=filename, Bucket=S3_BUCKET_NAME, Key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    # local_folder_path = './data/'
    # file_list = os.listdir(local_folder_path)
    # result_list = list(map(lambda s: local_folder_path + s, file_list))
    # counter = 0
    # print(result_list)
    # print(len(result_list))
    # print(result_list[1])