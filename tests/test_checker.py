import pytest
from aiohttp import ClientSession
from url_checker.checker import check_method

@pytest.mark.asyncio
async def test_check_method():
    async with ClientSession() as session:
        method, status = await check_method(session, 'https://www.google.com', 'GET', timeout=5)
        assert method == 'GET'
        assert status is not None

