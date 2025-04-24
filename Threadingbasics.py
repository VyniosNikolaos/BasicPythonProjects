import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("All workers finished")

if __name__ == "__main__":
    main()

"""
This script demonstrates basic threading concepts:
1. Creating threads with the Thread class
2. Starting threads
3. Waiting for threads to complete using join()

Key points:
- threading.Thread(): Creates a new thread
- thread.start(): Begins the thread's execution
- thread.join(): Waits for the thread to complete

Applications:
1. Executing multiple tasks concurrently
2. Improving responsiveness in I/O-bound applications
3. Parallel processing of independent tasks
"""