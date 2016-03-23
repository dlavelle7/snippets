#!/usr/bin/env python

import os
import sys


# TODO: Separate snippet?
def get_repo_root_dir():
    """Find root directory of current git repo

    If the current working directory is not in a git repo, print error and
    exit. Assuming that a git repo will always contain a .git directory
    and .gitignore / README.md files.
    """
    root_dirs = ['.git']
    root_files = ['.gitignore', 'README.md']
    current = os.getcwd()
    while current != "/":
        allnames = os.listdir(current)
        if all(root_dir in allnames for root_dir in root_dirs) and \
                all(root_file in allnames for root_file in root_files):
            return current
        else:
            current = os.path.abspath(os.path.join(current, os.pardir))
    print "The current working directory is not a git repository."
    sys.exit(1)

def reverse_walk(bottom):
    """Opposite of os.walk()

    Walks up the directory tree from 'bottom' path yielding a 3-tuple (dirpath,
    dirnames, filenames). Note: this differs from bottom-up option of os.walk
    which is a depth first version of os.walk(topdown=True)
    """
    while bottom != "/": # TODO or bottom != walk_until?
        dirnames = [f for f in os.listdir(bottom) if os.path.isdir(os.path.join(bottom, f))]
        filenames = [f for f in os.listdir(bottom) if os.path.isfile(os.path.join(bottom, f))]
        yield bottom, dirnames, filenames
        bottom = os.path.abspath(os.path.join(bottom, os.pardir))

print get_repo_root_dir()

for dirpath, dirnames, filenames in reverse_walk(os.getcwd()):
    print dirpath, dirnames, filenames
