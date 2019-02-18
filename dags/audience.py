from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import papermill as pm

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2013, 1, 1),
    'email': ['tamkien.duong@data.gouv.fr'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('audience', default_args=default_args, schedule_interval="@yearly")

def fetch_matomo(**kwargs):

    year = kwargs['execution_date'].year
    
    pm.execute_notebook(
        '/home/tk/etalab/notebooks/data.gouv.fr/audience/year-days.ipynb',
        '/home/tk/s3/notebooks/auto/audience/{}.ipynb'.format(year),
        parameters = { "year": year }
    )

def update_datagouvfr(ds, **kwargs):

    year = kwargs['execution_date'].year
    
    pm.execute_notebook(
        '/home/tk/etalab/notebooks/data.gouv.fr/audience/dgfr.update.ipynb',
        '/home/tk/s3/notebooks/auto/audience/dgfr.update-{}.ipynb'.format(year),
        parameters = { "year": year }
    )

fetch = PythonOperator(
    task_id="fetch_matomo",
    provide_context=True,
    python_callable=fetch_matomo,
    dag=dag
)

store = PythonOperator(
    task_id="update_datagouvfr",
    provide_context=True,
    python_callable=update_datagouvfr,
    dag=dag    
)

fetch >> store