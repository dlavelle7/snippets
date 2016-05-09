"""Some examples of how to use threading in Python"""
import threading


lock = threading.RLock()  # shared lock


class LockExample(object):
    """Reentry Lock example for threading with a shared resource (counter)."""

    def __init__(self):
        self.counter = 0

    def print_and_increment(self):
        # compare without lock!
        with lock:
            print self.counter
            self.counter += 1


example_obj = LockExample()
for i in range(20):
    thread = threading.Thread(target=example_obj.print_and_increment)
    thread.start()


# Thread waiting on event example
event = threading.Event()


def safe_print(message):
    """Lock otherwise print may be interrupted"""
    with lock:
        print message


def wait():
    safe_print("%s is waiting for event . . ." % threading.current_thread())
    event.wait()
    safe_print("{0} is free!".format(threading.current_thread()))


def set_event():
    safe_print("{0} is going to fire event".format(threading.current_thread()))
    event.set()


thread1 = threading.Thread(target=wait)
thread1.start()

thread2 = threading.Thread(target=set_event)
thread2.start()

thread1.join()  # Main thread waits for thread1 to terminate
