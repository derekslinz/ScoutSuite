from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.sgw.gateways import Gateways


class SGW(AliyunCompositeResources):
    _children = [
        (Gateways, 'gateways')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
