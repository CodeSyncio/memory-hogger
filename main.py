import random , psutil , time, os, sys
list = []

def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')  
if len(sys.argv) == 1:
     
    memfloodamount = input('amount of memory to pump full (MB):\n')
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
    
while (psutil.Process().memory_info().rss / (1024 * 1024)) < int(memfloodamount):
    randomstrink = 1
    for i in range(10000000):
        list.append(randomstrink)
    cls()
    print(f'Current Amount: {round(psutil.Process().memory_info().rss / (1024 * 1024))} megabytes')
   
    
cls()   
print(f'done , {psutil.Process().memory_info().rss / (1024 * 1024)} mb of memory is beeing kept\n')
while True:
    input('press enter to release memory...')
    break

del list
cls()
input('all memory has been released, press enter to quit...')