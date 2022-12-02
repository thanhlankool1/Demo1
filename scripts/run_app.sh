#!/bin/bash
base_dir=$(pwd)
gunicorn_path="$base_dir/venv/bin/gunicorn"
gunicorn_config_path="$base_dir/etc/gunicorn_conf_web_app.py"

run_command="$gunicorn_path -k uvicorn.workers.UvicornWorker -c $gunicorn_config_path app.main:app"

stop_app(){
        kill -9 `ps -ef | grep celery  | grep -v grep | awk '{print $2}'`
}
stop_app

celery_start(){
    echo `$celery_path`
    `$celery_path -A app.utils.celery worker --loglevel=info --detach`
}
echo "Start Celery"
$celery_start


echo "$run_command"
eval $run_command
