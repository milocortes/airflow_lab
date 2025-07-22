import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonVirtualenvOperator, is_venv_installed

log = logging.getLogger(__name__)

with DAG(
    dag_id = "tutorial_pandas",
    schedule=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    tags=["example"]
) as dag:
    if not is_venv_installed():
        log.warning("The virtualenv_pythom example tash requiress virtualenv, please install it")
    else:
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["pandas==2.1.1"], system_site_packages=False
        )

        def pandas_head():
            import pandas as pd
            csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
            df = pd.read_csv(csv_url, index_col=0)
            head = df.head(10)

            return head.to_csv()

        pandas_task = pandas_head()


