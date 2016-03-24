from multiprocessing import Pool, Process, Lock
import time
def f(x):
    return x*x
def g(l, i):
    l.acquire()
    print 'hello world', i
    time.sleep(1)
    l.release()

if __name__ == '__main__':
	start = time.time()
	p = Pool(5)
	print(p.map(f, [1, 2, 3,4,5,6,7,8,9,10]))
	print time.time()-start

	start = time.time()
	for i in range(1,4):
		print f(i)
	print time.time()-start, "\n \n------"

	lock = Lock()

	for num in range(10):
		Process(target=g, args=(lock, num)).start()
		print num