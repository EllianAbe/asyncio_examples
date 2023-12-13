import asyncio
from datetime import datetime
import timer


async def async_sleep(i):
    """
    Asynchronously sleeps for  seconds.

    Args:
        i (int): just a identifier.

    Returns:
        None
    """
    print("Starting... ", i, ' at ', datetime.now())
    await asyncio.sleep(3)


async def my_async_function():
    """
    An asynchronous function that performs async_sleep() for 10 times.

    Example usage:
        await my_async_function()
    """
    futures_list = [async_sleep(i) for i in range(10)]
    await asyncio.gather(*futures_list)


@timer.stopwatch
def main():
    asyncio.run(my_async_function())
