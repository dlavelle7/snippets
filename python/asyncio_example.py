import time
import asyncio
import datetime


async def custom_sleep():
    """E.g an I/O operation that takes a long time."""
    print("Sleeping {0}.".format(datetime.datetime.now()))
    await asyncio.sleep(1)  # event loop will execute next task while waiting


async def process(number):
    print("Processing data: {0}".format(number))
    await custom_sleep()
    print("Finished processing data: {0}".format(number))


loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(process(1)),
    asyncio.ensure_future(process(2)),
    asyncio.ensure_future(process(3)),
]

print("Running tasks . . .")
loop.run_until_complete(asyncio.wait(tasks))
print("Closing loop.")
loop.close()
