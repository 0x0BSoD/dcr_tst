#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Run Dev Server"
    exec python "identidock.py"
elif [ "$ENV" = 'UNIT' ]; then
    echo "Run Dev Tests"
    exec python "tests.py"   
else
    echo "Run Prod Server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9191
fi