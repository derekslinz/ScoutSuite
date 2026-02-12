from ScoutSuite.providers.aliyun.resources.iot import IoT as IoTResources
from ScoutSuite.providers.base.resources import ResourcesBase


class IoT(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = IoTResources(facade.iot)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
