#!/bin/bash
base_dir=$(pwd)
venv_path="$base_dir/venv"

if [ -d "$venv_path" ] 
then
    echo "Directory $venv_path exists. quit!" 
else
    echo "ENV $venv_path"
    # TODO: should add auto detect python version, should select lastest
    run_command="python3 -m venv venv"
    echo "command in here $run_command"
    eval $run_command
fi
