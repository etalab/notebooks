from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

import papermill as pm

notebooks =  Variable.get('notebooks')
buckets = Variable.get('buckets')

token =  Variable.get('token_etalab')
prod = True

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

dag = DAG('decp-json',
    default_args=default_args,
    catchup=False,
    schedule_interval=None
)

def token():
    f = open('{}/decp-json/datagouvfr-token.txt'.format(notebooks), "w+")
    f.write(token)
    f.close()

def sync():
    pm.execute_notebook(
        '{}/decp-json/decp-json.ipynb'.format(notebooks),
        '{}/notebooks/auto/decp-json/decp-json.ipynb'.format(buckets),
        parameters = { "PROD": prod }
    )

t0 = PythonOperator(
    task_id='token',
    python_callable=create_token,
    dag=dag
)

t1 = PythonOperator(
    task_id='sync',
    python_callable=sync,
    dag=dag
)

t0 >> t1
