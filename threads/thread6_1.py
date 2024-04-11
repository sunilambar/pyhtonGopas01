from multiprocessing import Process, Lock, Value, Manager
import time
def f(l, x, li):
  l.acquire()
  x.value += 1
  li.append(x.value)
  print(x.value)
  l.release()
  time.sleep(1)

if __name__ == '__main__':
  lock = Lock()
  n = Value('d', 0)
  manager = Manager()
  output_list=manager.list()
  sez = list()
  for i in range(10):
    sez.append(Process(target=f, args=(lock, n,output_list)))
    sez[i].start()

#  for i in range(10):
#    sez[i].join()
  for p in sez:
    p.join()
  print("Vysledna hodnota n:", n.value)
  print(output_list)
