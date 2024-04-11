# 'Chest-Cancer-classification End to  End Project 

## create env
conda create -p env python==3.9 -y
conda activate ./env

## package creation
pip install -r requirements.txt

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
MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
