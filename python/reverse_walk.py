#!/usr/bin/env python
import os


def get_repo_root_dir():
    """Return the root directory of current git repo

    If the current working directory is not in a git repo, print error and
    exit. Assuming that a git repo will always contain a .git directory
    and .gitignore / README.md files.
    """
    root_nodes = ['.gitignore', 'README.md', '.git']
    current = os.getcwd()
    while current != "/":
        allnames = os.listdir(current)
        if all(root_node in allnames for root_node in root_nodes):
            return current
        else:
            current = os.path.abspath(os.path.join(current, os.pardir))
    print "The current working directory is not a git repository."


def reverse_walk(bottom):
    """Walk up the directory tree and yield (dirpath, dirnames, filenames)

    Similar to os.walk() in reverse, but do not recurse over the
    subdirectories, just iterate back until root.
    """
    while bottom != "/":
        names = os.listdir(bottom)
        dirs = [f for f in names if os.path.isdir(os.path.join(bottom, f))]
        files = [f for f in names if os.path.isfile(os.path.join(bottom, f))]
        yield bottom, dirs, files
        bottom = os.path.abspath(os.path.join(bottom, os.pardir))


print get_repo_root_dir()

for dirpath, dirnames, filenames in reverse_walk(os.getcwd()):
    print dirpath, dirnames, filenames
