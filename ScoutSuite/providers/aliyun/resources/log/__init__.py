from .projects import Projects


class Log:
    def __init__(self, facade):
        self.facade = facade
        self.projects = Projects(self.facade)

    async def fetch_all(self, regions):
        await self.projects.fetch_all()
