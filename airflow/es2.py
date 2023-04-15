from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python_operator import PythonOperator

def current_datetime():
    print(datetime.now())

default_dag_args = {
    'start_date': datetime(2023, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1,
}

with DAG('Es_02_DAG', schedule_interval='@daily', catchup=False, default_args=default_dag_args) as dag_python:

    # Here we define our task
    task_00 = PythonOperator(task_id = 'print_current_datetime', python_callable = current_datetime())