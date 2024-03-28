#!/usr/bin/env python3
import sys
while True:
    try:
        text=input('Please enter your name: ')
    except EOFError:
        sys.exit(0)
    print(text.upper())
