#!/usr/bin/env bash
set -e

. ./env/Scripts/activate

PYTHONPATH=. python -m pytest test_runlengthfunctions.py

