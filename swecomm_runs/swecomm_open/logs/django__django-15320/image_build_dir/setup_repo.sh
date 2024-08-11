#!/bin/bash
set -euxo pipefail
git clone -o origin https://github.com/django/django /testbed
chmod -R 777 /testbed
cd /testbed
git reset --hard b55ebe32417e0884b6b8b3e1bc0379033aa221af
git remote remove origin
source /opt/miniconda3/bin/activate
conda activate testbed
echo "Current environment: $CONDA_DEFAULT_ENV"
python -m pip install -e .
