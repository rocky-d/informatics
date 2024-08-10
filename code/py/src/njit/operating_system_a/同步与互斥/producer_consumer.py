from threading import Thread
from threading import Lock
import time,random
pro_list = []
lock = Lock()
class Producer(Thread):
  def run(self):
    global pro_list
    while True:
      i = random.randint(0, 100)
      lock.acquire()
      if len(pro_list) > 0:
        print("!--product still in list, wait consumer to get it..")
      else:
        pro_list.append(i)
        print (":::Producer put:", pro_list[0])
      lock.release()
      time.sleep(2)
class Consumer(Thread):
  def run(self):
    global pro_list
    while True:
      lock.acquire()
      if len(pro_list) == 0:
        print( "!--No product now, wait producer put in...")
      else:
        print (":::Consumer fetch:", pro_list[0])
        pro_list.pop(0)
      lock.release()
      time.sleep(2)
Producer().start()
Producer().start()
Consumer().start()
Producer().start()
Producer().start()
Consumer().start()
Consumer().start()
