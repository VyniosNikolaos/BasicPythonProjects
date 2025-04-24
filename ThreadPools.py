import concurrent.futures
import time

def pool_worker(item):
    print(f"Processing {item}")
    time.sleep(1)
    return item * item

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(pool_worker, range(5)))
    print(f"Thread pool results: {results}")

if __name__ == "__main__":
    main()

"""
This script demonstrates the use of thread pools:
1. Creating a ThreadPoolExecutor
2. Submitting tasks to the pool
3. Collecting results from threaded executions

Key points:
- concurrent.futures.ThreadPoolExecutor: Manages a pool of worker threads
- executor.map(): Applies a function to an iterable in parallel
- With statement ensures proper cleanup of thread pool resources

Applications:
1. Efficiently managing a large number of similar tasks
2. Limiting the number of concurrent threads
3. Easily collecting results from parallel executions
"""