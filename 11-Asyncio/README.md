# Asyncio
Aysnio uses async keyword and gather to execute functions concurrently

## Comparison between Asyncio / Processes / Threads

1. Asyncio: for managing many awaiting tasks
2. for maximizing performance on cpu intensive tasks
3. for parallel tasks that share data with minimal cpu usage

Perfect example for asyncio:

```
import asyncio

async def task():
    print("Hi")
    await asyncio.sleep(1)
    print("Bye")

await asyncio.gather(task(),task(),task(),task(),task()) 

Output:
Hi
Hi
Hi
Hi
Hi
Bye
Bye
Bye
Bye
Bye
```

Another function : 

```
import asyncio

async def fetch(id, delay):
    print(f"Fetching data for id {id}")
    await asyncio.sleep(delay)
    return {"id":id, "data":"some data"}


async def main():
    t1 = asyncio.create_task(fetch(1, 2))
    t2 = asyncio.create_task(fetch(2, 3))
    t3 = asyncio.create_task(fetch(3, 1))

    r1 = await t1
    r2 = await t2
    r3 = await t3

    print(r1, r2, r3)

await main()

# Alternative way is to use gather to run functions concurrently
    
```
## Resources
https://replit.com/@codewithharry/96-Day-96-AsyncIO-in-Python#main.py