from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class SourceServers(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_servers = await self.facade.smc.get_source_servers()
        for raw_server in raw_servers:
            id, server = await self._parse_server(raw_server)
            self[id] = server

    async def _parse_server(self, raw_server):
        server_dict = {}
        server_id = raw_server.get('SourceId')
        
        server_dict['source_id'] = server_id
        server_dict['server_name'] = raw_server.get('SourceName')
        server_dict['status'] = raw_server.get('Status')
        server_dict['job_id'] = raw_server.get('JobId')
        server_dict['error_code'] = raw_server.get('ErrorCode')
        server_dict['error_message'] = raw_server.get('ErrorMessage')
        server_dict['cpu_cores'] = raw_server.get('CpuCores')
        server_dict['memory_size'] = raw_server.get('MemorySize')
        server_dict['os_type'] = raw_server.get('OsType')
        server_dict['platform'] = raw_server.get('Platform')
        server_dict['vcenter_id'] = raw_server.get('VCenterId')
        server_dict['created_time'] = raw_server.get('CreatedTime')
        server_dict['updated_time'] = raw_server.get('UpdatedTime')
        
        return server_id, server_dict
