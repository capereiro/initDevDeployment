#!/bin/bash

PARAM1=${1?Error: no name given}

function create() {
    python create.py
    echo "Hello! $PARAM1"
    echo "Hello! "
}

create