from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.cdn.domains import Domains


class CDN(AliyunCompositeResources):
    _children = [
        (Domains, 'domains')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
