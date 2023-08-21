#!/bin/bash

echo -e "AIRFLOW_UID=$(id -u)" > .env

# Set up Airflow using docker-compose (initialize Airflow database)
docker-compose up airflow-init

# Start Airflow and related services in detached mode
docker-compose up -d

# Define the name of the localstack container
CONTAINER_NAME="localstack_main"

# Execute the 'enter_container.sh' script inside the localstack container
docker exec -it $CONTAINER_NAME /tmp/localstack/enter_container.sh
