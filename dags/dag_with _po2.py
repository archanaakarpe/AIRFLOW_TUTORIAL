from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Archana',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(name, age):
    print(f"Hello World! My name is {name}, and I am {age} years old!")


with DAG(
    default_args=default_args,
    dag_id='our_first_dag_with_python_operator_v2',
    description='our first dag using python operator',
    start_date=datetime(2023, 2, 1),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name' : 'Archana', 'age' : '30'}
    )

    task1