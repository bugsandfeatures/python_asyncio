import asyncio 

async def f(): # first coroutine
	
	print("Running f")
	await asyncio.sleep(0)
	print("We're here again")


async def g(): # second coroutine

	print("Running g")
	await asyncio.sleep(0)
	print("Back to g")


async def main(): # 

	tasks = [
		f(),
		g()
	] # our tasks

	await asyncio.gather(*tasks) # if smth from tasks is coroutine it becomes a task 

asyncio.run(main())
