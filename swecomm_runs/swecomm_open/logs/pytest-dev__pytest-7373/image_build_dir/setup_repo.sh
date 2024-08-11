#!/bin/bash
set -euxo pipefail
git clone -o origin https://github.com/pytest-dev/pytest /testbed
chmod -R 777 /testbed
cd /testbed
git reset --hard 7b77fc086aab8b3a8ebc890200371884555eea1e
git remote remove origin
source /opt/miniconda3/bin/activate
conda activate testbed
echo "Current environment: $CONDA_DEFAULT_ENV"
python -m pip install -e .
