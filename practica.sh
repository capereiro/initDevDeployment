#!/bin/bash

PARAM1=${1?Error: agregar parametro}

python create.py # Ejecuta archivo .py desde una terminal
echo "Hello! $1"