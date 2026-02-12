from ScoutSuite.providers.aliyun.resources.sae import SAE as SAEResources
from ScoutSuite.providers.base.resources import ResourcesBase


class SAE(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = SAEResources(facade.sae)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
