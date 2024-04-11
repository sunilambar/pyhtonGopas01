import aiohttp
import asyncio

async def fetch(session, url):
    print(url)
    async with session.get(url) as response:
        return await response.text()

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(type(html))
        f=open(url[7:],'w',encoding='utf-8')
        #print(html)
        #f.write(bytes(html,'utf-8'))
        f.write(html)
        f.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(main('http://www.gopas.cz'),main('http://python.org')))
