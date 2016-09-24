#!/bin/bash

# Examples of bash parameter expansion

# 1. Get default shell variables ${variable:-default}
function foo {
    local value=${1:-foobar}  # if argument not passed, set a default
    echo $value
}

foo        # -> echos foobar
foo "bar"  # -> echos bar

# 2. Remove pattern from front of variable
# 2.1 Remove shortest part of pattern ${variable#pattern}
path=/a/b/c/b/d.txt

echo ${path#*/b/}  # -> echos c/b/d.txt (removes shorter pattern /a/b/)

# 2.2 Remove longest part of pattern ${variable##pattern}
echo ${path##*/b/}  # -> echos d.txt  (removes longer pattern /a/b/c/b/)

# 3. Remove pattern from end of variable
# 3.1 Remove shortest part of pattern ${variable%pattern}
file=foo.bar.baz

echo ${file%.ba*}  # -> echos foo.bar (removes shorter pattern .bar)

# 3.2 Remove longer part of pattern ${variable%%pattern)
echo ${file%%.ba*}  # -> echos foo (removes longer pattern .bar.baz)

# 4. Find and replace
# 4.1 Replace once (left to right) ${variable/pattern/replace}
var="bugs bunny bugs"
echo ${var/bugs/lola}  # -> echos 'lola bunny bugs'

# 4.2 Repplace all ${variable//pattern/replace}
echo ${var//bugs/lola}  # -> echos 'lola bunny lola'

# 5. Get the length of a string ${#variable}
robin="bravest"
echo ${#robin}  # -> echos 7

# 6. Display error message and stop execution ${variable:?Error message}
function bar {
    local res=${1:?"Error you did not pass an arg to bar()"}
}

bar "eggs"  # -> No Error
bar         # -> Throws an error with the given message

echo "This will never echo"  # Execution will stop at line 46 due to line 42
