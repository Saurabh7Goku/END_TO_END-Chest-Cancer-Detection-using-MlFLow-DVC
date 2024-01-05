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
