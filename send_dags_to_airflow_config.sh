#!/bin/bash
source airflow_config.sh

cp dags/*.py ${AIRFLOW_DAGS}

