from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Ensure Airflow can locate the src folder within the container plugins directory
sys.path.append('/opt/airflow/plugins')

from src.extract import fetch_market_data
from src.load import load_to_postgres

def main_etl():
    """
    Main execution function for the ETL pipeline.
    Handles data extraction and loading processes.
    """
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
    description='Automated ETL pipeline for crypto market data ingestion',
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['production', 'crypto', 'etl']
) as dag:

    task_etl = PythonOperator(
        task_id='run_full_etl',
        python_callable=main_etl
    )