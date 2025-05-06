from datatime import datatime
from airflow import DAG
from airflow.operators import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datatime(2025, 5, 7, 10, 00)
}

with DAG()