import _thread
import time
# Define a function for the thread
a=1
def print_time(threadName, delay):
  global a
  count = 0
  while count < 5:
    for i in range(delay*10_000_000):
      a+=1
    #time.sleep(delay)
    count += 1
    print("%s: %s" % (threadName, time.ctime(time.time())))

# Create two threads as follows
try:
  _thread.start_new_thread(print_time, ("Thread-1", 2,))
#  _thread.start_new_thread(print_time, ("Thread-2", 4,))
except Exception as ex:
  print("Error: unable to start thread")
  print(ex)
#while 1:
#  pass
x=input()
print(a)
