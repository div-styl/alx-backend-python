#!/usr/bin/env python3
"""
simple async func
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    await for a random number between 0 and max_delay which 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
