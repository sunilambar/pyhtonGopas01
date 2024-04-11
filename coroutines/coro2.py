import asyncio

#@asyncio.coroutine
async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    i= await asyncio.sleep(3.0)
    return x + y

#@asyncio.coroutine
async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))
print("main")
loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
