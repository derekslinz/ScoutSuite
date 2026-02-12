from ScoutSuite.providers.aliyun.resources.redis import Redis as RedisResources
from ScoutSuite.providers.base.resources import ResourcesBase


class Redis(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = RedisResources(facade.redis)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
