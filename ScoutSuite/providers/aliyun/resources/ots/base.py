from ScoutSuite.providers.aliyun.resources.ots import OTS as OTSResources
from ScoutSuite.providers.base.resources import ResourcesBase


class OTS(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = OTSResources(facade.ots)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
