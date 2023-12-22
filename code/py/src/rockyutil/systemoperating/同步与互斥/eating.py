import threading,time
rlock1 = threading.RLock()
rlock2 = threading.RLock()
rlock3 = threading.RLock()
rlock4 = threading.RLock()
rlock5 = threading.RLock()
class Zhexuejia():
    def __init__(self,left,right):
        self.left = left
        self.right = right
z1 = Zhexuejia(rlock5,rlock1)
z2 = Zhexuejia(rlock1,rlock2)
z3 = Zhexuejia(rlock2,rlock3)
z4 = Zhexuejia(rlock3,rlock4)
z5 = Zhexuejia(rlock4,rlock5)


def run(z,name):
    f=z.left.acquire()
    if f:
        print(name,"获取左筷子")
    ff = z.right.acquire()
    if ff:
        print(name,"获取有筷子")
        print("哲学家开始就餐",name)
        time.sleep(1)
    z.right.release()
    z.left.release()

t1 = threading.Thread(target=run,args=(z1,"z1"))
t2 = threading.Thread(target=run,args=(z2,"z2"))
t3 = threading.Thread(target=run,args=(z3,"z3"))
t4 = threading.Thread(target=run,args=(z4,"z4"))
t5 = threading.Thread(target=run,args=(z5,"z5"))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
