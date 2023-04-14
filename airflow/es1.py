from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_dag_args = {
    'start_date': datetime(2023, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1,
}

with DAG('Exercise_01_DAG', schedule_interval=None, default_args=default_dag_args) as dag:

    task_01 = BashOperator(task_id='bash_task', bash_command="echo 'command executed from bash operator'")
    task_02 = BashOperator(task_id='copy_file', bash_command="cp /home/carlo/airflow/DATA/RAW_DATA/raw.txt /home/carlo/airflow/DATA/CLEAN_DATA")
    task_03 = BashOperator(task_id='remove_file', bash_command="rm -r /home/carlo/airflow/DATA/RAW_DATA/raw.txt")

    task_01 >> task_02 >> task_03