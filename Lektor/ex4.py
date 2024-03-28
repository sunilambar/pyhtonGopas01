#!/usr/bin/env python3
import sys
filename=input('Enter path to file with names: ')
try:
    file=open(filename,'rt')
except OSError as ex:
    print('Error occured',ex.errno,type(ex),ex)
    sys.exit(1)
for name in file:
    print(name.rstrip().upper())
