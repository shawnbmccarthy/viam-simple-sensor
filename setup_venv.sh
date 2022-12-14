#!/bin/bash

python3 -m venv ./venv
. ./venv/bin/activate
python -m pip install -r ./requirements.txt
deactivate