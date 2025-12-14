# starter-code.py

import asyncio
import aiohttp
import time

URLS = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.wikipedia.org',
    'https://www.github.com',
    'https://www.stackoverflow.com'
]

# Async function to fetch a single URL
def save_content(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            content = await response.read()
            save_content(url.replace('https://', '').replace('.', '_') + '.html', content)
            print(f"Downloaded {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Async download took {time.time() - start:.2f} seconds")

# Students: Add a sequential version and performance comparison as described in the assignment.
