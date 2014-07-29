import os, time
def counter(count):                                    # run in new process
    for i in range(count):
        time.sleep(1)                                  # simulate real work
        print('[%s] => %s' % (os.getpid(), i))

import pdb;pdb.set_trace()
for i in range(5):
    pid= os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)              # in parent: continue
    else:
        counter(5)                                     # else in child/new process
        os._exit(0)                                    # run function and exit

print('Main process exiting.')  
