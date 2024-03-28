#!/usr/bin/env python3
import sys
#get filename from program parameter (parameter on command line)
print(sys.argv)
filename=sys.argv[1]
try:
    file=open(filename,'rt')
except OSError as ex:
    print('Error occured',ex.errno,type(ex),ex)
    sys.exit(1)
for name in file:
    print(name.rstrip().upper())
