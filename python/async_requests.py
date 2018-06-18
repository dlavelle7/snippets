#!/usr/bin/env python3
"""Asynchronous (aiohttp) request client - Python 3.6."""
from asyncio import get_event_loop
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError


async def async_request(request_method, url, **request_kwargs):
    async with request_method(url, **request_kwargs) as response:
        data = await response.json()
        try:
            response.raise_for_status()
        except ClientResponseError as exc:
            # raise_for_status() doesn't get body the response body
            exc.response_body = data
            raise
        return data


async def async_post(session, url, json):
    return await async_request(session.post, url, json=json)


async def async_get(url, session, params=None):
    params = {} if params is None else params
    return await async_request(session.get, url, params=params)


async def async_get_paged_results(url, session, params=None):
    """
    Async generator function to get the complete results set of a django rest
    framework endpoint.
    """
    while url:
        results = await async_get(url, session, params)
        url = results.get("next")
        params = None  # original params are in "next" url
        for result in results["results"]:
            yield result


async def make_async_requests(urls):
    async with ClientSession() as session:
        for url in urls:
            try:
                results = await async_get(url, session)
                print(f"Success: {results['count']} results")
            except ClientResponseError as exc:
                print(f"Error: {exc.response_body}")


async def make_async_get_paged_requests(url):
    async with ClientSession() as session:
        all_results = [x async for x in async_get_paged_results(url, session)]
    print(f"Length of all results {len(all_results)}")


if __name__ == "__main__":
    urls = [
        "https://uo-db-api.herokuapp.com/uo/users",
        "https://uo-db-api.herokuapp.com/uo/users",
    ]
    loop = get_event_loop()

    # Example of async get requests
    loop.run_until_complete(make_async_requests(urls))

    # Example of async generator function
    loop.run_until_complete(make_async_get_paged_requests(urls[0]))
