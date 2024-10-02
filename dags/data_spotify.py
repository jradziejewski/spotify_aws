import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.spotify_pipeline import spotify_pipeline

default_args = {"owner": "Jakub", "start_date": datetime(2024, 10, 2)}

file_postfix = datetime.now().strftime("%Y-%m-%d")

dag = DAG(
    dag_id="etl_spotify_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["spotify"],
)

extract = PythonOperator(
    task_id="extraction",
    python_callable=spotify_pipeline,
    op_kwargs={
        "file_name": f"spotify_{file_postfix}",
        "time_filter": "day",
        "limit": 100,
    },
    dag=dag,
)
