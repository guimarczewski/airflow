# airflow
Repo to study Airflow

# airflow astronomer setup with CLI
curl -sSL install.astronomer.io | sudo bash -s

https://docs.astronomer.io/astro/cli/get-started-cli

astro dev init

astro dev start

------

Postgres
https://renatogroffe.medium.com/postgresql-docker-compose-criando-rapidamente-ambientes-e-populando-bases-para-testes-6c4b9a4de313


Docker containers:
cloudbeaver
postgres-postgres-1
airflow-astronomer_bc4b7f-webserver-1
airflow-astronomer_bc4b7f-triggerer-1
airflow-astronomer_bc4b7f-postgres-1

docker network create pipeline
docker network connect pipeline postgres-postgres-1
docker network inspect pipeline

Criar o script de execução - script linux para subir containers automaticamente - setup.sh - comando "chmod 777 setup.sh" para transformar o arquivo em executável