from .applications import Applications


class SAE:
    def __init__(self, facade):
        self.facade = facade
        self.applications = Applications(self.facade)

    async def fetch_all(self, regions):
        for region in regions:
            await self.applications.fetch_all(region=region, service_account=None)
