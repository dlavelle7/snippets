"""Mutiprocessing example.

Sort the contents of a list by sleeping for the duration of their value.

THIS IS NOT AN ACTUAL SORTING ALGORITHM.

After sleeping, the subprocess adds it's value to a shared Array.

IN MULTIPROCESSING YOU SHOULD AVOID SHARING STATE BETWEEN PROCESSES.

But this is just for fun!
"""
import os
import time

from multiprocessing import Process, Manager


def sleep_for_n(n, sorted_list):
    pproc_id = os.getppid()
    proc_id = os.getpid()
    print(f"Sub process (id: {proc_id}, parent: {pproc_id}) sleeping for {n}")
    # sleep for n secs, then add to sharted list
    time.sleep(n)
    sorted_list.append(n)
    print(f"Sub process (id: {proc_id}, parent: {pproc_id}) appended {n}")


def sort(unsorted):
    print(f"Parent python process (id: {os.getpid()}).")
    with Manager() as manager:
        # create a list that can be shared between processes
        shared_list = manager.list([])
        processes = [Process(target=sleep_for_n, args=(element, shared_list,))
                     for element in unsorted]
        # start all the processes
        for p in processes:
            p.start()
        # parent process (like threading) to wait until all sub procs finished
        for p in processes:
            p.join()

        print(f"Sorted: {shared_list}")


sort([0.5, 0.2, 0.1, 0.4])
