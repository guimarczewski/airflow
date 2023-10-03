#!/usr/bin/env bash
up() {

  echo "Starting postgres..."
  cd postgres
  docker-compose up -d
  cd ..

  echo "Starting dbeaver..."
  cd dbeaver
  cd docker-cloudbeaver
  docker-compose up -d
  cd ..
  cd ..

  echo "Starting Airflow..."
  cd airflow-astronomer
  astro dev start
  cd ..
 
  echo "Access DBeaver at http://localhost:9090 and set up the connections."
  
  echo "Access Airflow at http://localhost:8080 to kick off your Airbyte sync DAG."  

  echo "Access Metabase at http://localhost:3000 and set up a connection with Snowflake."

}

config() {

  #curl -sSL install.astronomer.io | sudo bash -s

  docker network create pipeline
  docker network connect pipeline cloudbeaver
  docker network connect pipeline postgres-postgres-1
  docker network connect pipeline airflow-astronomer_bc4b7f-webserver-1
  docker network connect pipeline airflow-astronomer_bc4b7f-triggerer-1
  docker network connect pipeline airflow-astronomer_bc4b7f-postgres-1
  
  echo "Config Updated..."
}


down() {
  echo "Stopping Airflow..."
  cd airflow-astronomer
  astro dev stop
  cd ..

  echo "Stopping dbeaver..."
  cd dbeaver
  cd docker-cloudbeaver
  docker-compose down
  cd ..
  cd ..

  echo "Stopping postgres..."
  cd postgres
  docker-compose down
  cd ..
}

case $1 in
  up)
    up
    ;;
  config)
    config
    ;;
  down)
    down
    ;;
  *)
    echo "Usage: $0 {up|config|down}"
    ;;
esac