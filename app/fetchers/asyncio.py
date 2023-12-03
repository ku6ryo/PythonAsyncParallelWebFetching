import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def para_fetch(urls: str):
    async with aiohttp.ClientSession() as session:
        html_contents = await asyncio.gather(*(fetch(session, url) for url in urls))
    return html_contents
