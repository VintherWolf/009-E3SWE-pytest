#!/usr/bin/env bash
set -e

. ./env/Scripts/activate

PYTHONPATH=. python -m test_runlengthfunctions