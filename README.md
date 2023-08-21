* mkdir ./data

put the database.csv into the data folder

* chmod +x startup.sh
* chmod +x enter_container.sh
* sudo ./startup.sh

_________________
Configure your AWS profile by entering the Localstack container:

aws configure --profile default

* aws_access_key_id: test
* aws_secret_access_key: test 
* region: ap-southeast-1


_____________________________________
Create a bucket for the task: 

awslocal s3 mb s3://task10 

awslocal s3api list-buckets

awslocal s3 ls s3://task10

awslocal s3 rm s3://task10 --recursive
