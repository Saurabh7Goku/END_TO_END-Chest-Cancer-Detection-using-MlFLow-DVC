# Chest-Cancer-Detection

### Project WorkFlows...

    1. Update config.yaml
    2. Update params.yaml
    3. Update the entity
    4. Updaye the configuration manager in src config
    5. Update the components
    6. Update the Pipeline
    7. Update the main.py
    8. Update the dvc.yaml

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- MlFlow ui

### dagshub

[dagshub official Website](https://dagshub.com/)

Run this to export as env variables:

- `For Windows use **set** instead of export`

```bash

    export MLFLOW_TRACKING_URI=https://dagshub.com/Saurabh7Goku/END_TO_END-Chest-Cancer-Detection-using-MlFLow-DVC.mlflow

    export MLFLOW_TRACKING_USERNAME=Saurabh7Goku

    export MLFLOW_TRACKING_PASSWORD=🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈🙈

```

### DVC cmd

    1. dvc init
    2. dvc repro
    3. dvc dag

## About MLflow & DVC

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & taging your model

DVC

- Its very lite weight for POC only
- lite weight expriements tracker
- It can perform Orchestration (Creating Pipelines)

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 259588875913.dkr.ecr.eu-north-1.amazonaws.com/chest_cancer_classifier

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
