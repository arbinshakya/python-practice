import asyncio



async def load_data():
    print("loading..")
    await asyncio.sleep(5)
    print("data loaded")




async def task():
    print("Hello..")
    await asyncio.sleep(1)
    print("I am here")



async def main():
    await asyncio.gather(load_data(), task())

asyncio.run(main())