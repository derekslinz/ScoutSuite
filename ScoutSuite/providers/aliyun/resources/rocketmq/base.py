from ScoutSuite.providers.aliyun.resources.rocketmq import RocketMQ as RocketMQResources
from ScoutSuite.providers.base.resources import ResourcesBase


class RocketMQ(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = RocketMQResources(facade.rocketmq)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
