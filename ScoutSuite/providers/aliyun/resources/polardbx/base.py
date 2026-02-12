from ScoutSuite.providers.aliyun.resources.polardbx import PolarDBX as PolarDBXResources
from ScoutSuite.providers.base.resources import ResourcesBase


class PolarDBX(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = PolarDBXResources(facade.polardbx)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
