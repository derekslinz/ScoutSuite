from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.fnf.workflows import Workflows


class FNF(AliyunCompositeResources):
    _children = [
        (Workflows, 'workflows')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
