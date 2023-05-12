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
