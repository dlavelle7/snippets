Student Records
===============

Question
--------

All input files will be contained in a folder named input

All output files must be stored to a folder named output, which will exist.

Results for module marks are contained in folders for each block (1-4)

Results take the form

<StudentID><Mark>

and are contained in files named <modulecode>.txt

There is also a file named Students.txt containing:

<StudentID><Surname> <name><Birthdate><Address>

on each line.

You must produce student records for each student. These must be contained in a folder named <StudentID>

There must be:

* a file named Details.txt containing student details

* a file for each block containing results for that block, in the form:

    <ModuleID> <Mark>

* a file named notes.txt, if applicable containing:

    Failed:

    <ModuleID>

Testing
-------
* ./create_records.sh
* diff -r output/ test/expected/
