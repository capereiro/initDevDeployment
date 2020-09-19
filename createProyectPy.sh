#!/bin/bash

PARAM1=${1?Error: no name given}

echo "*** Creating new Python project called $1! ***"
# python3 create.py $1 # Ejecuta archivo .py desde una terminal
source .env
echo $FILEPATH$1
cd $FILEPATH$1

git init
# git remote add origin git@github.com:$USERNAME/$1.git

touch README.md
git add README.md
git commit -m "first AUTO-commit"
git branch -M master
git remote add origin https://github.com/$USERNAME/$1.git
git push -u origin master

# git remote add origin https://github.com/capereiro/charlys.git
# git remote add origin https://github.com/$USERNAME/$1.git
# touch README.md
# git branch -M master
# git push -u origin master