#!/bin/bash

# tak skazat configuration
aws configure --profile default

# Set AWS environment variables
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
aws configure set aws_session_token test
export AWS_SESSION_TOKEN=test

# Create S3 bucket using awslocal (assuming you have awslocal installed)
awslocal s3 mb s3://task10