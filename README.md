# Apache Airflow Lab

## Create virtual environment
Run the command:
```bash
uv init --python 3.11
```

## Apache Airflow Installation
Install Apache Airflow:
```bash
uv add apache-airflow apache-airflow-providers-fab
```

Setup environment variables
```bash
source ./airflow_config.sh
```
## Update Airflow configuration
### Create Airflow Configuration file
```bash
uv run airflow config list --defaults > "${AIRFLOW_HOME}/airflow.cfg"
```

### Update following configurations
Update executor to be ```LocalExecutor``` as default is ```sequentialExecutor```:

```bash
executor = LocalExecutor
```

Also add auth manager if you want to create a user using ```airflow users```.

```bash
auth_manager = airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
```

Create JWT secret key using following command:
```bash
openssl rand -base64 32
```
> In python you can run:
> ```python
> python -c "import secrets; print(secrets.token_urlsafe(32))"
> ```

Update JWT secret in config file.
```bash
jwt_secret = <YOUR_JWT_SECRET>
```

If you want CSRF token enabled generate another JWT token and update config file as follows:

```bash
secret_key =  <YOUR_JWT_SECRET>
```

## Setting up and testing airflow
Run the following to setup airflow
```bash
uv run airflow db migrate

uv run airflow users create \
    --username admin \
    --firstname milo \
    --lastname cortes \
    --role Admin \
    --email hermilocg@hotmail.com
```

## Launch Airflow

```bash
uv run airflow api-server --port 8080
```
