# deep Classifier project

## workflow

1. Update config.yaml
2. Update secrets.yaml (optional) <- This is a file having credentials like keys, password, id, etc
3. Update paramaters.yaml <- all parameters like training params, testing params, epochs, etc
4. Update the src entity (in src folder) <- entity means for e.g named tuple
5. Update the configuration manager in src config
6. Update the components. <- data ingestion and all other
7. Update the pipeline
8. Test run the pipeline stage
9. Run tox for testing your package
10. Update the dvc.yaml file <-it is like main.py
11. run "dvc reproduce" for running all the stages in pipeline

![](https://raw.githubusercontent.com/KadamSujit/FSDS_NOV_deepCNNClassifier/master/docs/images/Data%20Ingestion%402x.png)


# to run in cmd/gitbash terminal for local machine
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./artifacts \
--host 0.0.0.0 -p 1234




STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/KadamSujit/FSDS_NOV_deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=KadamSujit \
MLFLOW_TRACKING_PASSWORD=7a6c3d8d82f747a0f5c203b2a1eece52804c583f \
python script.py



STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model