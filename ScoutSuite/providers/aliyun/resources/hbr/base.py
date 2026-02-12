from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.hbr.vaults import Vaults


class HBR(AliyunCompositeResources):
    _children = [
        (Vaults, 'vaults')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
