import json
import pathlib

import pendulum
import requests
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
from requests.exceptions import ConnectionError, MissingSchema

import psycopg2
from datetime import datetime, timedelta, timezone

def _get_data_api():
    # Define connection
    conn = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password="password",
        port = "5424"
    )

    # Making a get request
    response = requests.get('http://127.0.0.1:8000')

    # print json content
    json_val = response.json() 
    print(json_val)

    valor = json_val["valor"]

    # 
    random_date = datetime.now(timezone.utc)

    cur = conn.cursor()
    cur.execute("INSERT INTO stock_prices_fastapi (time, ticker, price) VALUES (%s, %s, %s)", (random_date, "APL", valor))

    conn.commit()

with DAG(
    dag_id="populate_table",
    description="Obten datos de la API y envíalo a la db.",
    start_date=pendulum.today("UTC").add(days=-1),
    #schedule="@daily",
    schedule="*/1 * * * *",
    catchup=True,
):

    get_data_api = PythonOperator(task_id="get_data_api", python_callable=_get_data_api)

    get_data_api
