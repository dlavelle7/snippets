"""Example of how to use subprocesses.Popen to spawn new subproceess"""

from subprocess import Popen, PIPE
import traceback


def create_process(cmd_string):
    try:
        process = Popen(cmd_string, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        print "Executing command: '%s'" % cmd_string
        stdoutdata, stderrdata = process.communicate()

        if process.returncode:
            print "Error: Command failed with returncode %s" % process.returncode
            if stderrdata:
                print stderrdata
        else:
            print stdoutdata

    except TypeError:
        print "Error: Invalid command argument type"
    except Exception as e:
        traceback.print_exc()
        print "Error: An unexpected error occurred"


create_process("foo bar baz")  # piped stderr
create_process("ls -la")
