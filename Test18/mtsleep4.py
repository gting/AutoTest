#coding=utf-8
import threading
from time import sleep, ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        super(ThreadFunc, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:',ctime())
    threads = []
    nloops = range(len(loops))
    # 创建线程
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    # 开始线程
    for i in nloops:
        threads[i].start()
    # 等待所有线程结束
    for i in nloops:
       threads[i].join()

    print('all end:', ctime())

if __name__ == '__main__':
    main()