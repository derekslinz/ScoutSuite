from ScoutSuite.providers.aliyun.resources.drds import DRDS as DRDSResources
from ScoutSuite.providers.base.resources import ResourcesBase


class DRDS(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = DRDSResources(facade.drds)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
