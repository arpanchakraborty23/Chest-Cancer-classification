# Chest-Cancer-classification End to  End Project 

## Problem Statement
This project aims to develop a web API for classifying chest cancer based on patient health data, providing an early diagnostic tool to support healthcare professionals in treatment planning and preventative care.

## Goal
 
Built a chest cancer classification web API using Image data of patient  to enable doctors early diagnosis and support treatment planning

## create env
```bash
conda create -p env python==3.9 -y
conda activate ./env
```

## package creation
```bash
pip install -r requirements.txt
```

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml

## src
1. Data Ingestion
2. Base Model
3. Model Train
4. Model Evaluation

## Dagshub
```bash
MLFLOW_TRACKING_URI=""
MLFLOW_TRACKING_USERNAME=""
MLFLOW_TRACKING_PASSWORD=""
```
## How to run?
### STEPS:
Clone the repository
```bash
https://github.com/entbappy/End-to-End-Chicken-Disease-Classification-using-Fecal-Image.git
```
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -n env python=3.12 -y
conda activate ./env
```
### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
## Run  App
```bash
python app.py
```

## AWS-CICD-Deployment-with-Github-Actions
```bash
1. Login to AWS console.
2. Create IAM user for deployment
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
3. Create ECR repo to store/save docker image
- Save the URI: 586343447297.dkr.ecr.us-east-1.amazonaws.com/chestcancer
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  586343447297.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = chest-cancer-app
```
