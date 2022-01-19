#!/bin/bash

until   nc -z -v -w30 db 5432
do
  echo 'Waiting for database connection'
  sleep 0.5
done


alembic upgrade head
uvicorn 'app.app:create_app' --host='0.0.0.0' --port=5000 --reload
