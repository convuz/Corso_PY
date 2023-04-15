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

with DAG('Es_01_DAG', schedule_interval=None, default_args=default_dag_args) as dag:

    task_0 = BashOperator(task_id='bash_task', bash_command="echo 'command executed from bash operator'")
    task_1 = BashOperator(task_id='copy_file', bash_command="cp /mnt/c/Users/riccardo/Desktop/corso_programmazione/DATA_CENTER/DATA_LAKE/dataset_raw.txt /mnt/c/Users/riccardo/Desktop/corso_programmazione/DATA_CENTER/DATA_CLEANED")
    task_2 = BashOperator(task_id='remove_file', bash_command="rm -r /mnt/c/Users/riccardo/Desktop/corso_programmazione/DATA_CENTER/DATA_LAKE/dataset_raw.txt")

    task_0 >> task_1 >> task_2
