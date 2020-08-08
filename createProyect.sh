#!/bin/bash

PARAM1=${1?Error: no name given}

echo "*** Welcome to bash scripting interpreter $1! ***"
python create.py $1 # Ejecuta archivo .py desde una terminal
# mkdir $1