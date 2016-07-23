#!/bin/bash

# Get this scripts dir. Alternately: SCRIPT_DIR=$(dirname $(realpath $0))
SCRIPT_DIR=${0%/*}  # Note: sh & ./ will give different $0

# Cleanup old output first
rm -r $SCRIPT_DIR/output > /dev/null 2>&1  # redirect output and error
mkdir $SCRIPT_DIR/output

function write_student_resuts {
    # Get block name, alternative to: block_name=$(basename $1)
    strip_slash=${1%/}  # remove trailing slash
    block_name=${strip_slash##*/}  # remove leading path
    student_block_path=${2}/${block_name}_results.txt
    for module in $1*.txt; do
        # Alternatively: module_name=$(basename $module .txt)
        module_filename=${module##*/}
        module_name=${module_filename%.txt}
        # Find this students results for each module
        while read -r result_line; do
            IFS=' ' read -a result_array <<< "$result_line"
            if [ "${result_array[0]}" = $student_id ]
            then
                module_result="${result_array[1]}"
                # Append module result to this block (double >> appends)
                echo $module_name $module_result >> $student_block_path
                # Check if this student has failed
                check_for_failures $module_result $2 $module_name
                break  # Student result found, move on
            fi
        done < $module
    done
}

function check_for_failures {
    # Check if the student failed
    if [ $1 -lt 40 ]
    then
        notes_file_path=${2}/notes.txt
        # If this is the first found failure, create notes.txt
        if [ ! -f $notes_file_path ]
        then
            echo 'Failed:' > $notes_file_path
        fi
        # Append the failed module result
        echo $3 >> $notes_file_path
    fi
}

# Loop over each student
while read -r student; do
    # Get next student details
    IFS=' ' read -a student_array <<< "$student"  # could do: array=($student)
    student_id="${student_array[0]}"

    # Create output for that student
    student_dir="${SCRIPT_DIR}/output/$student_id"
    mkdir $student_dir
    # Write details for that student (single > writes new)
    echo "${student}" > $student_dir/Details.txt

    # Loop over the blocks and modules to find this students results
    for block_path in ${SCRIPT_DIR}/input/*/; do
        write_student_resuts $block_path $student_dir
    done

done < "${SCRIPT_DIR}/input/Students.txt"
