from ScoutSuite.providers.aliyun.resources.memcache import Memcache as MemcacheResources
from ScoutSuite.providers.base.resources import ResourcesBase


class Memcache(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = MemcacheResources(facade.memcache)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
