from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Supaya Airflow bisa nemu folder src di dalam container
sys.path.append('/opt/airflow/plugins')

from src.extract import fetch_market_data
from src.load import load_to_postgres

def main_etl():
    """Fungsi utama yang menjalankan aliran ETL"""
    data = fetch_market_data()
    load_to_postgres(data)

default_args = {
    'owner': 'caelan',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='crypto_market_ingestion_pro_v1',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task_etl = PythonOperator(
        task_id='run_full_etl',
        python_callable=main_etl
    )