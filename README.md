# Apache Airflow Lab

## Create virtual environment
Run the command:
```bash
python3 -m venv .venv
```

Activate venv:
```bash
source .venv/bin/activate
```

## Apache Airflow Installation
Load environment variables:
```bash
source constraints.sh
```

Or install Airflow with pip:
```bash
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

## Airflow
Run standalone:
```bash
airflow standalone
```