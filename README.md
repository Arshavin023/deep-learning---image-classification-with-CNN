# deep-learning---image-classification-with-CNN


## Workflows

1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update dvc.yaml
10. app.py


# How to run?

### STEPS:

CLone the repository

```bash
https://github.com/Arshavin023/deep-learning---image-classification-with-CNN
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```


### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```


```
##### cmd
- mlflow ui

```

### dagshub
[dagshub](https://dagshub.com/),

MLFLOW_TRACKING_URI=https://dagshub.com/Arshavin023/deep-learning---image-classification-with-CNN.mlflow
MLFLOW_TRACKING_USERNAME=Arshavin023
MLFLOW_TRACKING_PASSWORD=3a6add494bc8a69b0623dd2f8030d353dde15622

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Arshavin023/deep-learning---image-classification-with-CNN.mlflow
export MLFLOW_TRACKING_USERNAME=Arshavin023
export MLFLOW_TRACKING_PASSWORD=3a6add494bc8a69b0623dd2f8030d353dde15622
```

```windows
set MLFLOW_TRACKING_URI=https://dagshub.com/Arshavin023/deep-learning---image-classification-with-CNN.mlflow
set MLFLOW_TRACKING_USERNAME=Arshavin023
set MLFLOW_TRACKING_PASSWORD=3a6add494bc8a69b0623dd2f8030d353dde15622
```

### DVC cmd
dvv init
dvc repro
dvc dag