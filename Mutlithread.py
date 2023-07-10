from multiprocessing.pool import ThreadPool
from threading import currentThread,Lock
import time
def work(obj,l=None):
    with l:
        obj[0] += 1
        print('当前线程是:',currentThread().name,':',obj)
        time.sleep(0.5)
    return obj
def main():
    l = Lock()
    mylist = [1]
    p = ThreadPool(10)
    #print(help(ThreadPool))
    res = []
    for var in range(10):
        # res.append(p.apply(func=work,args=(mylist,l)))
        res.append(p.apply_async(func=work,args=(mylist,l)))
    p.close() #关闭进程池
    p.join()
    #print(res) #apply
    for var in res: #apply_async
      	print(var.get(),end=' ')
    print('\nover')
if __name__ == '__main__':
		main()
