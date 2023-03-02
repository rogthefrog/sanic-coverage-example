#!/usr/bin/env bash

virtualenv -p python3.9 venv
source venv/bin/activate
pip install -r requirements.txt
coverage run
coverage xml