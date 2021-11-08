import aiohttp
from .config import Config

_LIST_URL = 'https://tapi.thuhole.com/v3/contents/post/list?page={page}&device=0&v=v3.0.6-454554'
_DETAIL_URL = 'https://tapi.thuhole.com/v3/contents/post/detail?pid={pid}&device=0&v=v3.0.6-454554'

async def get_list(page: int):
    async with aiohttp.ClientSession(headers=Config().get_token()) as session:
        async with session.get(_LIST_URL.format(page=page)) as resp:
            ret = await resp.json()
    if ret['code'] != 0:
        raise Exception(ret['msg'])
    return ret


async def get_detail(pid: str):
    async with aiohttp.ClientSession(headers=Config().get_token()) as session:
        async with session.get(_DETAIL_URL.format(pid=pid)) as resp:
            ret = await resp.json()
    if ret['code'] != 0:
        raise Exception(ret['msg'])
    return ret
