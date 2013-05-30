import sys
print sys.argv
import threading
def worker():
    print threading.currentThread().getName(),'staring'
    print threading.currentThread().getName(),'Exiting'
t = threading.Thread(name='worker', target=worker)
print t.start()