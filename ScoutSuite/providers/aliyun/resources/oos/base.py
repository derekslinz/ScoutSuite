from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.oos.templates import Templates
from ScoutSuite.providers.aliyun.resources.oos.tasks import Tasks


class OOS(AliyunCompositeResources):
    _children = [
        (Templates, 'templates'),
        (Tasks, 'tasks')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
