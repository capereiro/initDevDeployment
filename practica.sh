#!/bin/bash

PARAM1=${1?Error: no name given}

python create.py # Ejecuta archivo .py desde una terminal
echo "Hello! $1"