from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

import papermill as pm

notebooks =  Variable.get('notebooks')
buckets = Variable.get('buckets')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('IRVE',
    default_args=default_args,
    catchup=False,
    schedule_interval=None
)

def fetch_list():
    pm.execute_notebook(
        '{}/irve/liste.ipynb'.format(notebooks),
        '{}/notebooks/auto/irve/liste.ipynb'.format(buckets)
    )

def download():
    pm.execute_notebook(
        '{}/irve/download.ipynb'.format(notebooks),
        '{}/notebooks/auto/irve/download.ipynb'.format(buckets)
    )

def consolidation():
    pm.execute_notebook(
        '{}/irve/consolidation.ipynb'.format(notebooks),
        '{}/notebooks/auto/irve/consolidation.ipynb'.format(buckets)
    )

def dgfr():
    pm.execute_notebook(
        '{}/irve/dgfr.update.ipynb'.format(notebooks),
        '{}/notebooks/auto/irve/dgfr.update.ipynb'.format(buckets)
    )

def s3():
    pm.execute_notebook(
        '{}/irve/s3.push.ipynb'.format(notebooks),
        '{}/notebooks/auto/irve/s3.push.ipynb'.format(buckets)
    )
t1 = PythonOperator(
    task_id='list',
    python_callable=fetch_list,
    dag=dag
)

t2 = PythonOperator(
    task_id='download_resources',
    python_callable=download,
    dag=dag
)

t3 = PythonOperator(
    task_id='consolidation',
    python_callable=consolidation,
    dag=dag
)

t4 = PythonOperator(
    task_id='update_data.gouv.fr',
    python_callable=dgfr,
    dag=dag
)

t5 = PythonOperator(
    task_id='push_s3',
    python_callable=s3,
    dag=dag
)


t1 >> t2 >> t3 >> [t4,t5]
