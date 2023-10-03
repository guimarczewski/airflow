import pandas as pd

def join_tables(dag, **kwargs):
    # Carrega os dados das duas tabelas
    df1 = pd.read_sql("SELECT NomeEstado, IdRegiao FROM Estados", con=kwargs['postgres_conn'])
    df2 = pd.read_sql("SELECT IdRegiao, NomeRegiao FROM Regioes", con=kwargs['postgres_conn'])

    # Faz o join das tabelas
    df_joined = df1.merge(df2, on='IdRegiao')

    # Salva os dados da tabela unida
    df_joined.to_sql('tabela_unida', con=kwargs['postgres_conn'], if_exists='replace')

join_tables_task = PythonOperator(
    task_id='join_tables',
    python_callable=join_tables,
    op_kwargs={
        'postgres_conn': 'basegeografica'
    },
    dag=dag
)
