from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.resources.dbs.backup_plans import BackupPlans
from ScoutSuite.providers.aliyun.resources.dbs.restore_plans import RestorePlans


class DBS(AliyunCompositeResources):
    _children = [
        (BackupPlans, 'backup_plans'),
        (RestorePlans, 'restore_plans')
    ]

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
