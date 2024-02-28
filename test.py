import threading
from time import sleep
thusk = 1
b = True;
def p():
    global thusk
    global b
    thusk = 1
    while b:
        
        print(thusk)
        thusk += 1

def q():
    global thusk
    global b
    while b:
        print(thusk)
        thusk -=1
        
        
t1 = threading.Thread(target=p)
t2 = threading.Thread(target=q)


t1.start()
t2.start()

sleep(2)
b = False
t1.join()
t2.join()



        
