from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Workflows(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_workflows = await self.facade.fnf.get_flows()
        for raw_workflow in raw_workflows:
            id, workflow = await self._parse_workflow(raw_workflow)
            self[id] = workflow

    async def _parse_workflow(self, raw_workflow):
        workflow_dict = {}
        flow_name = raw_workflow.get('Name')
        
        workflow_dict['name'] = flow_name
        workflow_dict['definition'] = raw_workflow.get('Definition')
        workflow_dict['description'] = raw_workflow.get('Description')
        workflow_dict['status'] = raw_workflow.get('Status')
        workflow_dict['created_at'] = raw_workflow.get('CreatedAt')
        workflow_dict['updated_at'] = raw_workflow.get('UpdatedAt')
        workflow_dict['role_arn'] = raw_workflow.get('RoleArn')
        
        # Get detailed information
        details = await self.facade.fnf.get_flow(flow_name)
        if details:
            workflow_dict['type'] = details.get('Type')
            workflow_dict['version_id'] = details.get('VersionId')
            workflow_dict['last_modified_time'] = details.get('LastModifiedTime')
            
        # Get execution history
        executions = await self.facade.fnf.get_execution_history(flow_name)
        workflow_dict['recent_executions'] = executions
        workflow_dict['has_failed_executions'] = any(
            ex.get('Status') == 'Failed' for ex in executions
        )
        
        return flow_name, workflow_dict
