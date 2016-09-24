#!/bin/bash

# Example of bash arrays and how to debug bash scripts

# Execute your script with `bash -x my_script.sh` to trace its execution
# Use `set -x` in your bash script to trace its execution

function associative_array {
    # Associative array
    local -A my_array=( ["Lola"]="Bunny" ["Roy"]="Keane" )
    my_array["Foo"]="Bar"

    # Array length
    echo "Length of associative_array ${#my_array[*]}"

    # Loop over populated indices
    for key in ${!my_array[*]}
    do
        echo "Key: ${key} Value: ${my_array[$key]}"
    done
}

function linear_array {
    # Declare my_array variable of type linear array
    declare -a my_array=( "spam" [1]="eggs" )
    # Unassigned indicies are unset by bash
    my_array[5]="camelot"

    # Array length
    echo "Length of linear array ${#my_array[*]}"

    # Loop over contents of array
    for value in ${my_array[@]}
    do
        echo "Value: ${value}"
    done

    # Forget about my_array variable when you're done (same as local)
    unset my_array
}

# Active debugging for function call and deactivate
set -o xtrace
associative_array
set +o xtrace

# The following code will not be traced
linear_array
