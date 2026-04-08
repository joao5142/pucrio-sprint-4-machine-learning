#!/bin/sh
set -e

echo "Iniciando API Flask"
flask run --host=0.0.0.0 --port=${PORT:-3001} 