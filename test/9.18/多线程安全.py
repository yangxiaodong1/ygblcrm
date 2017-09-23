# Author : July  Yang
import time
from threading import Thread
import threading


val = 0
lock = threading.Lock()
def fun():
    global val
    lock.acquire()
    val+=1
    lock.release()

for i in range(100):
    t =threading.Thread(target=fun,args=(i,))
    t.start()










