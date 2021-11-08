import asyncio

async def f():
	
	print("Running f")
	await asyncio.sleep(0)
	print("We're here again")


async def pb():

	print("Content to pb")
	await asyncio.sleep(0)
	print("Back to pb")


async def main():

	tasks = [
		f(),
		pb()
	]

	await asyncio.gather(*tasks)

asyncio.run(main())