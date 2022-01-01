import asyncio


async def sleep_a_little(time_to_sleep):
    await asyncio.sleep(time_to_sleep)


async def go_do_something():
    time_to_sleep = 1
    await sleep_a_little(time_to_sleep)


asyncio.run(go_do_something())
