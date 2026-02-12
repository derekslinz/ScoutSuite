from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.smc.source_servers import SourceServers
from ScoutSuite.providers.aliyun.resources.smc.replication_jobs import ReplicationJobs


class SMC(AliyunCompositeResources):
    _children = [
        (SourceServers, 'source_servers'),
        (ReplicationJobs, 'replication_jobs')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
