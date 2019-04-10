import multiprocessing 
import time
import os
import signal
import sys

def workers_quit(signum, frame):
	for worker in proc_list:
		os.kill(worker.pid, signal.SIGKILL)
	sys.exit()

def fun(name):
	while True:
		print("process %s running,process name: worker_%s"%(os.getpid(), name))
		time.sleep(2)


if __name__ == "__main__":
	signal.signal(signal.SIGINT, workers_quit)
	signal.signal(signal.SIGTERM, workers_quit)
	proc_list = []
	for i in range(3):
		worker = multiprocessing.Process(target = fun, name = 'worker_%s'%i, args =(i,))
		proc_list.append(worker)
		worker.start()
	time.sleep(6)
	print("kill worker_1")
	for worker in proc_list:
		if worker.name == "worker_0":
			os.kill(worker.pid, signal.SIGKILL)
			proc_list.remove(worker)
	print(proc_list)
	for worker in proc_list:
		worker.join() 



