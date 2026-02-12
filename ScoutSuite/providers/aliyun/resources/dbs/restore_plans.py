from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class RestorePlans(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_plans = await self.facade.dbs.get_restore_plans()
        for raw_plan in raw_plans:
            id, plan = await self._parse_plan(raw_plan)
            self[id] = plan

    async def _parse_plan(self, raw_plan):
        plan_dict = {}
        plan_id = raw_plan.get('RestorePlanId')
        
        plan_dict['restore_plan_id'] = plan_id
        plan_dict['restore_plan_name'] = raw_plan.get('RestorePlanName')
        plan_dict['source_type'] = raw_plan.get('SourceType')
        plan_dict['status'] = raw_plan.get('Status')
        plan_dict['created_time'] = raw_plan.get('CreatedTime')
        plan_dict['updated_time'] = raw_plan.get('UpdatedTime')
        plan_dict['start_time'] = raw_plan.get('StartTime')
        plan_dict['completion_percentage'] = raw_plan.get('CompletionPercentage')
        
        return plan_id, plan_dict
