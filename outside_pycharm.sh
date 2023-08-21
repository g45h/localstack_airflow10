#!/bin/bash

# Change to the directory of the script
cd "$(dirname "$0")"

# Activate the virtual environment (assumes venv is in the script's directory)
source venv/bin/activate

# Install Python dependencies from requirements.txt in the virtual environment
pip install -r requirements.txt

# Specify the directories you want to create
directories=("./config" "./logs" "./plugins")

# Check if each directory exists, and create it if it doesn't
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "Creating directory: $dir"
        mkdir "$dir"
    else
        echo "Directory $dir already exists."
    fi
done

echo -e "AIRFLOW_UID=$(id -u)" > .env

