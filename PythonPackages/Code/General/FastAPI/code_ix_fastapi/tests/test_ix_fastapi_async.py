import asyncio
from httpx import AsyncClient
import pytest
import time

from ix_fastapi import app


@pytest.mark.asyncio
async def test_01_counter_normal():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:5000") as ac:
        response = await ac.get("/counter_normal")
    assert response.status_code == 200
    assert response.json().get('counter') == "normal counter"
    assert 2.95 < response.json().get('time') < 3.2


async def normal_counter_call():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:5000") as ac:
        response = await ac.get("/counter_normal")

@pytest.mark.asyncio
async def test_02_counter_normal_multi():
    s = time.perf_counter()
    await asyncio.gather(normal_counter_call(), normal_counter_call(), normal_counter_call())
    elapsed = time.perf_counter() - s

    assert 8.9 < elapsed < 9.5

@pytest.mark.asyncio
async def test_03_counter_async():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:5000") as ac:
        response = await ac.get("/counter_async")
    assert response.status_code == 200
    assert response.json().get('counter') == "async counter"
    assert 0.98 < response.json().get('time') < 1.2

async def async_counter_call():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:5000") as ac:
        response = await ac.get("/counter_async")

@pytest.mark.asyncio
async def test_04_counter_async_multi():
    s = time.perf_counter()
    await asyncio.gather(async_counter_call(), async_counter_call(), async_counter_call())
    elapsed = time.perf_counter() - s

    assert 0.9 < elapsed < 1.1
