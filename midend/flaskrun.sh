#!/bin/bash
export FLASK_APP=hello.py
python -m flask run --host=0.0.0.0 --port=9090
