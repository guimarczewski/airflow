from airflow import dag
from datetime import datetime
# operador da task utilizando python, cada ,engine tem um
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json

def captura_conta_dados():
	# quantidade de dados
	url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
	response = requests.get(url)
	df = pd.DataFrame(json.load(response.content))
	qtd = len(df.index)
	return qtd

# ti = task instance - pega info da captura_conta_dados
def e_valida(ti):
	if (qtd > 1000):
		qtd = ti.xcom_pull(task_ids = 'captura_conta_dados')
		return 'valida'
	return 'n_valida'

with DAG('tutorial_dag', start_date = datetime(2021,12,1), 
            schedule_interval = '30 * * * *', catchup = False) as dag:
	# parâmetros: id, inicio execução, intervalo de execução, catchup = True
	# ele cria dags para todos os dias entre o inicio e hoje
	
	captura_conta_dados = PythonOperator(
		task_id = 'captura_conta_dados',
		python_callable = captura_conta_dados # nome função
	)
	e_valida = BranchPythonOperator(
		task_id = 'e_valida',
		python_callable = e_valido
	)
	
	#verificar se a qtd está ok ou não bashoperator, se der valido ou não vai mudar o caminho
	valido = BashOperator(
		task_id = 'valido',
		bash_command = "echo 'Quantidade ok'"
	)
	
	nvalido = BashOperator(
		task_id = 'nvalido',
		bash_command = "echo 'Quantidade não ok'"
	)

# define a ordem de execução pelo task_id
captura_conta_dados >> e_valida >> [valido, nvalido]