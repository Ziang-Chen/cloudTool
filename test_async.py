import asyncio
import time


async def main0():
    print("hello0")
    time.sleep(1)
    print("world0")


async def main1():
    print("hello1")
    time.sleep(1)
    print("world1")


asyncio.run(main0())
asyncio.run(main1())
