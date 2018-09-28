# -*- coding: utf-8 -*-

import multiprocessing
from multiprocessing import Manager
import time
import os, random, datetime

from flask import Flask

def write_info(q):
    print("Process %s is write ..." % os.getpid())
    for i in range(100):
        q.put(str(i))
        print("put %s to queue" % str(i))
        #time.sleep(random.random())


def pro_read(q):
    print("Process %s is read ..." % os.getpid())
    while True:
        if q.empty():
            #print("the queue is empty Process %s"% os.getpid())
            #print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)
        else:
            num = q.get()
            if str(num) == '1':
                q.put('1+1')
            else:
                print("get %s from queue. Process %s" %(str(num), os.getpid()))


print("parent pid %s" % str(os.getpid()))
pool = multiprocessing.Pool(processes=2)
mng = Manager()
queue = mng.Queue()
app = Flask(__name__)


@app.route('/hello/<num>')
def hello1(num=None):
    queue.put(str(num))
    return 'hello i\'am hear you 11111', 200


@app.route('/hello')
def hello():
    queue.put('world')
    return 'hello i\'am hear you', 200




# write_info(q=queue)

    # work1 = multiprocessing.Process(target= pro_read, args=(queue, ))
    # work2 = multiprocessing.Process(target= pro_read, args=(queue, ))
    # work1.start()
    # work2.start()
    #
    # work1.join()

    # work2.join()

results = []
for i in range(2):
    ret = pool.apply_async(pro_read, args=(queue, ))
    results.append(ret)

# print("work is done!")
# time.sleep(10)
# write_info(q=queue)
# time.sleep(100)

app.run(port=8080)


