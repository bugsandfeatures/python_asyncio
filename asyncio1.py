import asyncio 

async def f(): # first coroutine
	
	print("Running f")
	await asyncio.sleep(0)
	print("We're here again")


async def pb(): # second coroutine

	print("Content to pb")
	await asyncio.sleep(0)
	print("Back to pb")


async def main(): # 

	tasks = [
		f(),
		pb()
	] # our tasks

	await asyncio.gather(*tasks) # if smth from tasks is coroutine it becomes a task 

asyncio.run(main())
