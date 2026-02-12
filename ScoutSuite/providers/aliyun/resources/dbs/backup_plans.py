from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class BackupPlans(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_plans = await self.facade.dbs.get_backup_plans()
        for raw_plan in raw_plans:
            id, plan = await self._parse_plan(raw_plan)
            self[id] = plan

    async def _parse_plan(self, raw_plan):
        plan_dict = {}
        plan_id = raw_plan.get('PlanId')
        
        plan_dict['plan_id'] = plan_id
        plan_dict['plan_name'] = raw_plan.get('PlanName')
        plan_dict['source_type'] = raw_plan.get('SourceType')
        plan_dict['status'] = raw_plan.get('Status')
        plan_dict['database_type'] = raw_plan.get('DatabaseType')
        plan_dict['created_time'] = raw_plan.get('CreatedTime')
        plan_dict['updated_time'] = raw_plan.get('UpdatedTime')
        plan_dict['begin_timestamp'] = raw_plan.get('BeginTimestamp')
        plan_dict['end_timestamp'] = raw_plan.get('EndTimestamp')
        plan_dict['backup_policy'] = raw_plan.get('BackupPolicy')
        plan_dict['incremental_backup_period'] = raw_plan.get('IncrementalBackupPeriod')
        
        return plan_id, plan_dict
