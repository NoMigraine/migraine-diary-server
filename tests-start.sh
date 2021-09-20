#! /usr/bin/env bash
set -e

export DEPLOY_ENV=TEST

python app/initial_db.py

# Run migrations
alembic upgrade head

python app/initial_data.py
python app/tests_pre_start.py

#bash ./scripts/test.sh "$@"
