import os
from multiprocessing import Process
import time
i=123
def info(title):
  print(title)
  print('module name: '+ __name__)
  print('parent process: '+ str(os.getppid()))
  print('process id: '+ str(os.getpid()))
  print('')
def f(name):
  global i
  info('> function f')
  time.sleep(len(name))
  i+=1
  print('hello', name)
  print(i)

if __name__ == '__main__':
  info('> main line')
  p1 = Process(target=f, args=('bob',))
  p1.start()
  p2 = Process(target=f, args=('alice',))
  p2.start()
  #p.join()
  print("End >main line")
