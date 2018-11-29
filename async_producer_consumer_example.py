import asyncio
import math


async def produce_factorial(queue):
    n = 0
    while True:
        if queue.full():
            await asyncio.sleep(1)
        else:
            # item = math.factorial(n)
            item = await loop.run_in_executor(None, math.factorial, n)
            # расчитываю факториал и кладу в очередь.
            print(f"put item {item}")
            await queue.put(item)
            n += 1

            await asyncio.sleep(0.5)


async def consume_factorial(queue):
    while True:
        while not queue.empty():
             item = await queue.get()
             print(f'recieved {item}')
        else:
            print("wait for queue")
            await asyncio.sleep(1)


loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop, maxsize=3)
consumer_coro = consume_factorial(queue)
producer_coro = produce_factorial(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
loop.close()
