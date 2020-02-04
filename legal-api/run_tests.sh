#!/bin/sh
# run_tests.sh

set -e

cd /app
ls
env
pytest
exit