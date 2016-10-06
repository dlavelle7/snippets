"""Example of file locking using the fcntl module.

Script will write and remove a file to the same directory as this script.
"""

import os
import fcntl
import threading

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foo")


def atomic_write_new_version():
    """Increment the integer value in the file in an atomic fashion."""

    version_file = open(PATH, "r+")  # open file for updating (read & write)
    try:
        # Exclusive lock, other processes blocked when trying to acquire lock
        fcntl.flock(version_file, fcntl.LOCK_EX)
        try:
            try:
                old_version = int(version_file.read())  # read existing version
            except ValueError:
                old_version = 0  # e.g empty file, first update
            # Clear contents of file for updating
            version_file.seek(0)
            version_file.truncate()
            # Write new version
            new_version = old_version + 1
            version_file.write(str(new_version))
            # Ensure contents of file has been written to disk
            version_file.flush()  # flush internal buffers
            os.fsync(version_file.fileno())  # force write of file to disk
        finally:
            fcntl.flock(version_file, fcntl.LOCK_UN)  # explicit unlock
    finally:
        version_file.close()  # this implicitly unlocks the file
    print "Version updated from %s to %s" % (old_version, new_version)


# Setup
if not os.path.exists(PATH):
    with open(PATH, "w"):
        pass

# Example using threads - note the sequential incrementing of the version
for i in xrange(20):
    thread = threading.Thread(target=atomic_write_new_version)
    thread.start()

# Teardown
try:
    os.remove(PATH)
except IOError:
    pass
