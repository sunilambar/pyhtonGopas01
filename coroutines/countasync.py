#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    print("Pred sleep")
    await asyncio.sleep(1)
    print("Po sleep")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter() - s
    print(f"Trvalo to {e:0.4f} sekund.")
