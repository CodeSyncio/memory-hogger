import random , psutil , time, os, sys
from threading import local
from tkinter import Variable
from click import pause
list = []
from multiprocessing import Process, Queue
def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')  

def tasker(memory,listname,processname,q):
    
    listname = []
    while (psutil.Process().memory_info().rss / (1024 * 1024)) < int(memory):
        randomstrink = 1
        for i in range(10000000):
            listname.append(randomstrink)
        
    print(f'thread {processname} done , total mem: {round(psutil.Process().memory_info().rss / (1024 * 1024))} megabytes')    
    q.put(f'{processname}')
    time.sleep(99999)

if __name__ == '__main__':
    q = Queue()
    
    
    if len(sys.argv) == 1:
        
        memfloodamount = input('amount of memory to pump full (MB):\n')
        cls()
        print(f'memory limit set to {memfloodamount} , press enter to continue...')
        ghosty = input()
        cls()
        print('pumping will start in 3 seconds...')
        time.sleep(3)
        cls()
    
    else:
        memfloodamount = sys.argv[1]
        print(f'memory limit set to {memfloodamount}, starting to flood in 1 sec...')
        time.sleep(1)
        cls()
    
    partedmem = int(memfloodamount) /8
    process1 ='';process2 = '';process3 = '';process4 = '';process5 = '';process6 = '';process7 = '';process8 = ''
    
    testeke = [process1,process2,process3,process4,process5,process6,process7,process8]
    
    for i in range(len(testeke)):
        testeke[i] = Process(target=tasker, args=(partedmem,f'list{i}',f'process{i}',q))
        testeke[i].start()
        print(testeke[i])
    
    
    time.sleep(3)    
    cls()
    print('all child processes are working... please wait...')

    
    
    
    StatusChecker = []
    for i in range(8):
        
        StatusChecker.append(q.get())
    
    
    
    if len(StatusChecker) == 8:
        print('Received DONE signal from all child processes')
        pass
    else:
        print('something went wrong, quitting in 5 sec...')
        time.sleep(5)
        quit()
    time.sleep(3)
    cls()
    ghost = input('press enter to release memory...')
    cls()
    for i in range(len(testeke)):
        testeke[i].terminate()
        time.sleep(1)
        print(f'{testeke[i]}      |||continuing to next child...')
    
    
    time.sleep(3)
    cls()
    print('released memory sucessfully, press enter to quit...')
    dede = input()
    
    
   
   