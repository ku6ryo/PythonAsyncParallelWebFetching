Test of Python's async website fetching. Measured the time elapsed to fetch URLs.

Sync: Normal sycronized fetching. 
Async: Using asyncio
Thread Pool: Using ThreadPool

```
Sync: 0.7598023414611816
Async: 0.24415183067321777
Thread Pool: 0.237030029296875
```

# How to run
```
poetry install
python -m app.main
```