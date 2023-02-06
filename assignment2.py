from datetime import datetime, timedelta

from airflow import DAG
#from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner' : 'Archana',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='my_dag4',
    default_args=default_args,
    start_date=datetime(2023, 1, 6),
    schedule_interval='@once'
) as dag:

    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost1',
        sql="""
            create table if not exists employee (
                id int,
                first_name character varying,
                last_name character varying,
                primary key (id)
                )
            """
    )
  

    task2 = PostgresOperator(
        task_id='update_postgres_table',
        postgres_conn_id='postgres_localhost1',
        sql="""
          insert into employee (id, first_name, last_name)
           values('103', 'Avani', 'Karpe');
           """
        )
    task1 >> task2