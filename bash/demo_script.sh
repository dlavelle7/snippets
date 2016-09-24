#!/bin/bash

# Useful bash script for doing live demos

function wait_enter {
    local SZ=`stty size | cut -f1 -d' '`
    tput cup ${SZ} 0; read -p 'Press enter to continue . . .'
    clear
}

function run_and_show_command {
    local CMD=$1
    echo $CMD
    printf "\n"
    eval $CMD
}

clear

cat << __EOM__
Demo Heading
------------

Demo intro text here . . .

__EOM__

wait_enter

cat << __EOM__
List Files
----------

e.g list files in working directory:

__EOM__

run_and_show_command "ls -la"

wait_enter
