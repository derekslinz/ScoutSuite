from .instances import Instances


class Memcache:
    def __init__(self, facade):
        self.facade = facade
        self.instances = Instances(self.facade)

    async def fetch_all(self, regions):
        for region in regions:
            await self.instances.fetch_all(region=region, service_account=None)
