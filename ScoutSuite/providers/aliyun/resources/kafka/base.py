from ScoutSuite.providers.aliyun.resources.kafka import Kafka as KafkaResources
from ScoutSuite.providers.base.resources import ResourcesBase


class Kafka(ResourcesBase):
    def __init__(self, facade):
        super().__init__(facade)
        self.service = KafkaResources(facade.kafka)

    async def fetch_all(self, regions):
        await self.service.fetch_all(regions)
