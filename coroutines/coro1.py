import re
import asyncio
#@asyncio.coroutine
def regex_matcher(regex):
  print("Coroutine start")
  while True:
    text=(yield)
    if text is None: continue
    print('Received '+text)
    for match in regex.finditer(text):
      print(match.group())
      #print(dir(match))

regex=re.compile('a+')
r=regex_matcher(regex)
#print(type(r),dir(r))
print("Before next call on coroutine generator function")
x=next(r)
next(r)
#print(x)
r.send('anaaconda')
r.send('ahoj')
