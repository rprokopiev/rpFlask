import asyncio


async def sum_array(array):
    return sum(array)
 

async def asyncio_sum(array):
    result = await sum_array(array)
    return result
 

def asyncio_main(array):
    asyncio_result = asyncio.run(asyncio_sum(array))
    return asyncio_result

