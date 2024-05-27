import asyncio
import time
from fastapi import APIRouter

router = APIRouter()

# test of synchronous behaviour
def count():
    print("One")
    time.sleep(1)
    print("Two")

@router.get("/counter_normal")
async def counter_normal():
    s = time.perf_counter()
    for _ in range(3):
        count()

    elapsed = time.perf_counter() - s

    return {"counter": "normal counter", "time": elapsed}

# test of asynchronous behaviour
async def async_count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def async_count_starter():
    await asyncio.gather(async_count(), async_count(), async_count())

@router.get("/counter_async")
async def counter_async():
    s = time.perf_counter()

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        tsk = loop.create_task(async_count_starter())
        await tsk

    elapsed = time.perf_counter() - s

    return {"counter": "async counter", "time": elapsed}
