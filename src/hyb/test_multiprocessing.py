import os, time, random
from multiprocessing import Process, Pool

print('Process (%s) start...' % os.getpid())


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ =='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(6)
    for i in range(6):
        p.apply_async(long_time_task,args=('task('+str(i)+')',))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print('All subprocesses done.')

