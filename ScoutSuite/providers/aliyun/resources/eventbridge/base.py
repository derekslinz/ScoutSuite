from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.eventbridge.event_buses import EventBuses


class EventBridge(AliyunCompositeResources):
    _children = [
        (EventBuses, 'event_buses')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
