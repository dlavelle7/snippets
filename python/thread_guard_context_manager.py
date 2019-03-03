import threading
import time


class ThreadGuard(object):
    """Threading context manager which ensures all threads are finished."""

    def __init__(self):
        self.enter_threads = set()

    def __enter__(self):
        self.enter_threads.update(thread for thread in threading.enumerate())

    def __exit__(self, *args):
        exit_threads = set(thread for thread in threading.enumerate())
        leftover_threads = exit_threads - self.enter_threads
        for thread in leftover_threads:
            thread.join()


def foo(thread_id):
    time.sleep(3)
    print "Thread {0} finished".format(thread_id)


t1 = threading.Thread(target=foo, args=[1])
t2 = threading.Thread(target=foo, args=[2])

thread_guard = ThreadGuard()

with thread_guard:
    t1.start()
    t2.start()

print "Main thread done"
