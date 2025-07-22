import logging
from datetime import datetime, timedelta
from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.operators.python import PythonVirtualenvOperator, is_venv_installed

log = logging.getLogger(__name__)

RAW_WINE_DATASET = Dataset("file://localhost/aiflow/datasets/raw_wine_dataset.csv")

with DAG(
        dag_id = "wine_dataset_consumer",
        schedule = [RAW_WINE_DATASET],
        start_date = datetime(2023, 1, 1),
        tags = ["example"],
    ) as dag:

    if not is_venv_installed():
        #raise RuntimeError("virtualenv is not installed!")
        log.warning("The virtualenv_pythom example tash requiress virtualenv, please install it")

    else:
        @task.virtualenv(
            task_id = "virtualenv_python", requirements = ["pandas==2.1.1"],
            system_site_packages=False
        )
        def clean_dataset():
            import pandas as pd
            
            df = pd.read_csv("~airflow/datasets/raw_wine_dataset.csv", index_col = 0)
            df = df.replace({"\r":""}, regex=True)
            df = df.replace({"\n":""}, regex=True)
            df.drop(["grape"], axis = 1, inplace=True)

            df.to_csv("~/airflow/datasets/cleaned_dataset.csv")

        clean_dataset()
