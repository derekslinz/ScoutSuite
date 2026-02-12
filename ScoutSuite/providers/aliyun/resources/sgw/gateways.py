from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Gateways(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_gateways = await self.facade.sgw.get_gateways()
        for raw_gateway in raw_gateways:
            id, gateway = await self._parse_gateway(raw_gateway)
            self[id] = gateway

    async def _parse_gateway(self, raw_gateway):
        gateway_dict = {}
        gateway_id = raw_gateway.get('GatewayId')
        
        gateway_dict['gateway_id'] = gateway_id
        gateway_dict['gateway_name'] = raw_gateway.get('GatewayName')
        gateway_dict['gateway_type'] = raw_gateway.get('Type')
        gateway_dict['status'] = raw_gateway.get('Status')
        gateway_dict['region_id'] = raw_gateway.get('RegionId')
        gateway_dict['vswitch_id'] = raw_gateway.get('VSwitchId')
        gateway_dict['create_time'] = raw_gateway.get('CreatedDate')
        gateway_dict['last_heartbeat_time'] = raw_gateway.get('LastHeartbeatTime')
        gateway_dict['model'] = raw_gateway.get('GatewayModel')
        gateway_dict['local_file_upload_rate_limit'] = raw_gateway.get('LocalFileUploadRateLimit')
        gateway_dict['reverse_sync_path'] = raw_gateway.get('ReverseSyncPath')
        
        # Get detailed information
        details = await self.facade.sgw.get_gateway(gateway_id)
        if details:
            gateway_dict['location'] = details.get('Location')
            gateway_dict['ip_address'] = details.get('IpAddress')
            
        # Get cache configuration
        caches = await self.facade.sgw.get_gateway_caches(gateway_id)
        gateway_dict['caches'] = caches
        gateway_dict['cache_count'] = len(caches)
        
        return gateway_id, gateway_dict
