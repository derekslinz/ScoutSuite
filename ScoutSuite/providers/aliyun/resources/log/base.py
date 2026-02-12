from ScoutSuite.providers.aliyun.resources.log import Log as LogResources
from ScoutSuite.providers.base.resources import ResourcesBase


class Log(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = LogResources(facade.log)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
