#!/bin/bash


function run() {
    for i in $(seq 1 1000); do
        curl -s "http://127.0.0.1:8000/api/v1/users/" > /dev/null &
    done 

    wait
}

time run -h
