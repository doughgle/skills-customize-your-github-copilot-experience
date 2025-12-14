# 📘 Assignment: Asyncio Web Downloader

## 🎯 Objective

Learn to use Python's asyncio library to download multiple web pages concurrently. Practice asynchronous programming, error handling, and performance measurement.

## 📝 Tasks

### 🛠️ Set Up Asyncio Project

#### Description
Set up your Python environment and create a starter script for asynchronous web downloading.

#### Requirements
Completed setup should:

- Create a Python file (e.g., `downloader.py`)
- Import `asyncio` and `aiohttp` (install `aiohttp` if needed)
- Define a list of at least 5 URLs to download


### 🛠️ Implement Async Downloader

#### Description
Write an asynchronous function to download web pages concurrently using asyncio and aiohttp.

#### Requirements
Completed program should:

- Define an async function that fetches a single URL
- Use asyncio to schedule downloads for all URLs concurrently
- Save the content of each page to a separate file
- Handle and report errors for failed downloads


### 🛠️ Compare Performance

#### Description
Compare the performance of your async downloader with a sequential (non-async) version.

#### Requirements
Completed comparison should:

- Implement a sequential version of the downloader
- Measure and print the time taken by both approaches
- Write a short reflection on the benefits and challenges of async programming
