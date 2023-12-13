from datetime import datetime
import time
import timer


def sync_sleep(i):
    """
    Sleeps for 3 seconds and prints the current time and the given parameter.

    Parameters:
        i (int): The parameter to print along with the current time.

    Returns:
        None
    """
    print("Starting... ", i, ' at ', datetime.now())
    time.sleep(3)


def my_sync_function():
    """
    Sync function that sleeps 10 times for 3 seconds
    """
    futures_list = [sync_sleep(i) for i in range(10)]


@timer.stopwatch()
def main():
    my_sync_function()
