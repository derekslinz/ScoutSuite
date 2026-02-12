from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Tasks(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_tasks = await self.facade.oos.get_tasks()
        for raw_task in raw_tasks:
            id, task = await self._parse_task(raw_task)
            self[id] = task

    async def _parse_task(self, raw_task):
        task_dict = {}
        task_id = raw_task.get('TaskId')
        
        task_dict['task_id'] = task_id
        task_dict['template_name'] = raw_task.get('TemplateName')
        task_dict['status'] = raw_task.get('TaskStatus')
        task_dict['create_time'] = raw_task.get('CreateTime')
        task_dict['end_time'] = raw_task.get('EndTime')
        task_dict['outputs'] = raw_task.get('Outputs', {})
        task_dict['failure_reason'] = raw_task.get('FailureReason')
        
        return task_id, task_dict
