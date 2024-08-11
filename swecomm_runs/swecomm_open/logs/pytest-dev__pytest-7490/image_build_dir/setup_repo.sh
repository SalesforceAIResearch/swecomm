#!/bin/bash
set -euxo pipefail
git clone -o origin https://github.com/pytest-dev/pytest /testbed
chmod -R 777 /testbed
cd /testbed
git reset --hard 7f7a36478abe7dd1fa993b115d22606aa0e35e88
git remote remove origin
source /opt/miniconda3/bin/activate
conda activate testbed
echo "Current environment: $CONDA_DEFAULT_ENV"
python -m pip install -e .
