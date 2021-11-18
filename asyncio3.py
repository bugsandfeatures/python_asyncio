import random
from time import sleep
import asyncio

def task(n):
	rint = random.randint(0, 2) # generate random time

	sleep(rint)
	print('Task %s ended' % n, rint)


async def task_async(n): # the same is task(), but this is a coroutine
	rint = random.randint(0, 2)

	await asyncio.sleep(rint)
	print('Task %s ended' % n, rint)

def sync():
	for i in range(1, 10):
		task(i)


async def asyncfunc():
	tasks = [asyncio.ensure_future(task_async(i)) for i in range(1, 10)]
	await asyncio.wait(tasks)

print('Sync')
sync()

print('Async')

async def main():

	await asyncio.gather(asyncfunc())

asyncio.run(main())
































