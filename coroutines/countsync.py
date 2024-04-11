#!/usr/bin/env python3
# countsync.py

import time

def count():
    print("Pred sleep")
    time.sleep(1)
    print("Po sleep")

def main():
    for i in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    e = time.perf_counter() - s
    print(f"Trvalo to {e:0.4f} sekund.")
