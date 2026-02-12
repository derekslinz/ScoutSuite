from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Services(AliyunResources):
    def __init__(self, facade: AliyunFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        raw_services = await self.facade.fc.get_services(self.region)
        for raw_service in raw_services:
            id, service = await self._parse_service(raw_service)
            self[id] = service

    async def _parse_service(self, raw_service):
        service_dict = {}
        service_name = raw_service.get('ServiceName')
        
        service_dict['name'] = service_name
        service_dict['description'] = raw_service.get('Description')
        service_dict['status'] = raw_service.get('Status')
        service_dict['created_time'] = raw_service.get('CreatedTime')
        service_dict['updated_time'] = raw_service.get('UpdatedTime')
        service_dict['role_arn'] = raw_service.get('RoleArn')
        service_dict['log_config'] = raw_service.get('LogConfig', {})
        service_dict['vpc_config'] = raw_service.get('VpcConfig', {})
        service_dict['nas_config'] = raw_service.get('NasConfig', {})
        service_dict['tracing_config'] = raw_service.get('TracingConfig', {})
        
        # Get detailed information
        details = await self.facade.fc.get_service(service_name, self.region)
        if details:
            service_dict['version_id'] = details.get('VersionId')
            service_dict['last_modified'] = details.get('LastModified')
            
        # Get functions
        functions = await self.facade.fc.get_functions(service_name, self.region)
        service_dict['function_count'] = len(functions)
        service_dict['functions'] = functions
        
        return service_name, service_dict
