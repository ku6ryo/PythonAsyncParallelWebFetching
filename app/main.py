import time
import asyncio
from .fetchers.asyncio import para_fetch as para_fetch_async
from .fetchers.thread_pool import para_fetch as para_fetch_thread_pool
from .fetchers.sync import multi_fetch as multi_fetch_sync


urls = ["http://example.com", "http://example.org", "http://example.net"]

def main():
    sync_start = time.time()
    multi_fetch_sync(urls)
    sync_end = time.time()
    print(f"Sync: {sync_end - sync_start}")

    async_start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(para_fetch_async(urls))
    print(f"Async: {time.time() - async_start}")

    thread_pool_start = time.time()
    para_fetch_thread_pool(urls)
    print(f"Thread Pool: {time.time() - thread_pool_start}")

if __name__ == "__main__":
    main()