#!/bin/bash
base_dir=$(pwd)
gunicorn_path="$base_dir/venv/bin/python"
celery_path="$base_dir/venv/bin/celery"
run_command="$gunicorn_path run_app.py"

stop_app(){
        kill -9 `ps -ef | grep celery  | grep -v grep | awk '{print $2}'`
}
stop_app

celery_start(){
    echo "alo alo" 
    echo `$celery_path`
    `$celery_path -A app.utils.celery worker --loglevel=info`
}
echo "Start Celery"
nohup $celery_start

echo "$run_command"
eval $run_command