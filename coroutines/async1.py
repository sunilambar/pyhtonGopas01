import asyncio
i=1
async def gen(u=8):
  i = 0
  while i < u:
    yield 2 ** i
    i += 1
    await asyncio.sleep(.3)

async def tisknu_si():
  global i
  while i<30:
    print(f'Neco si tisknu a pocitam {i}')
    i+=1
    await asyncio.sleep(.5)
  #return i

async def main():
  g = [i async for i in gen()]
  print(g)
  f = [j async for j in gen() if not (j // 3 % 5)]
  print(f, sep="\n")
  #return g, f

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(main(),tisknu_si()))
loop.close()
