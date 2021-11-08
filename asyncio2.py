from time import time
import asyncio

start = time()

def tic(): # time display function

	return 'at %1.1f sec' % (time() - start)


async def f1():

	print(f'f1 started {tic()}')
	await asyncio.sleep(2)
	print(f'f1 ended {tic()}')


async def f2():

	print(f'f2 started {tic()}')
	await asyncio.sleep(2)
	print(f'f2 ended {tic()}')


async def f3():

	print(f'while other coroutines are blocked {tic()}') # while coroutines sleep 2 sec
	await asyncio.sleep(1)
	print('Done!')


async def main():

	tasks = [
		f1(), 
		f2(), 
		f3()
	]

	await asyncio.gather(*tasks)


asyncio.run(main())






