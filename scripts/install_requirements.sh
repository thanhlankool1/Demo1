#!/bin/bash
base_dir=$(pwd)
pip_path="$base_dir/venv/bin/pip"
requirement_path="$base_dir/etc/requirements.txt"

if [ -n "$http_proxy" ]
then
    run_command="$pip_path install -r $requirement_path --proxy $http_proxy"  
else
    run_command="$pip_path install -r $requirement_path"
fi

echo "$run_command"
eval "/demo_app/venv/bin/python3 -m pip install --upgrade pip"
eval $run_command