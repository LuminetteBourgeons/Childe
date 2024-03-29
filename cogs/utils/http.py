import asyncio
import aiohttp
from . import cache

class HTTPSession(aiohttp.ClientSession):
  def __init__(self, loop=None):
    super().__init__(loop=loop or asyncio.get_event_loop())
  def __del__(self):
    if not self.closed:
      self.close()

session = HTTPSession()

@cache.async_cache()
async def query(url, method="get", res_method="text", *args, **kwargs):
  async with getattr(session, method.lower())(url, *args, **kwargs) as res:
    return await getattr(res, res_method)()

async def get(url, *args, **kwargs):
  return await query(url, "get", *args, **kwargs)

async def post(url, *args, **kwargs):
  return await query(url, "post", *args, **kwargs)
