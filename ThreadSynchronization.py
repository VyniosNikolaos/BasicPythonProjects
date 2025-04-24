import threading

shared_resource = 0
lock = threading.Lock()

def increment():
    global shared_resource
    for _ in range(100000):
        with lock:
            shared_resource += 1

def decrement():
    global shared_resource
    for _ in range(100000):
        with lock:
            shared_resource -= 1

def main():
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Final shared resource value: {shared_resource}")

if __name__ == "__main__":
    main()

"""
This script illustrates thread synchronization:
1. Using locks to protect shared resources
2. Implementing mutual exclusion
3. Ensuring thread-safe operations

Key points:
- threading.Lock(): Creates a mutual exclusion lock
- with lock: Provides a context manager for acquiring and releasing the lock
- Protects critical sections to prevent race conditions

Applications:
1. Safely updating shared data in multi-threaded environments
2. Implementing thread-safe data structures
3. Coordinating access to limited resources
"""