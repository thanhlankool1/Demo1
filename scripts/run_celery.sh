#!/bin/bash
base_dir=$(pwd)
gunicorn_path="$base_dir/venv/bin/python"
celery_path="$base_dir/venv/bin/celery"


stop(){
        kill -9 `ps -ef | grep celery  | grep -v grep | awk '{print $2}'`
}


start(){
    echo $celery_path
    $celery_path -A app.utils.celery worker --loglevel=info #--detach
}

start