import asyncio

async def task1():
    print('send first email')
    asyncio.create_task(task2())
    await asyncio.sleep(2)
    print('first email replay')

async def task2():
    print('send second mail')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('second email reply')
    

async def task3():
    print('send third email')
    print('third email reply')
    print('end')

asyncio.run(task1())