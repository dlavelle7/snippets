#!/usr/bin/env python

import os
import sys


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

print get_repo_root_dir()
