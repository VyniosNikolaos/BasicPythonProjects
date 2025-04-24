import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        print(f"Thread {self.name} starting")
        time.sleep(3)
        print(f"Thread {self.name} finished")

def main():
    threads = [MyThread(str(i)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All class-based threads finished")

if __name__ == "__main__":
    main()

"""
This script shows how to create custom thread classes:
1. Subclassing the Thread class
2. Implementing a custom run() method
3. Creating and managing custom thread objects

Key points:
- Inherit from threading.Thread
- Override the run() method to define thread behavior
- Use start() to begin execution, which calls run()

Applications:
1. Encapsulating complex thread behavior
2. Creating reusable threaded components
3. Implementing thread-specific state and methods
"""