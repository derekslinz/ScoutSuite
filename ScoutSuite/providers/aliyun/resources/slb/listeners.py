from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Listeners(AliyunResources):
    def __init__(self, facade: AliyunFacade, region: str, load_balancer_id: str):
        super().__init__(facade)
        self.region = region
        self.load_balancer_id = load_balancer_id

    async def fetch_all(self):
        for raw_listener in await self.facade.slb.get_listeners(region=self.region, load_balancer_id=self.load_balancer_id):
            id, listener = await self._parse_listener(raw_listener)
            self[id] = listener

    async def _parse_listener(self, raw_listener):
        listener_dict = {}
        listener_dict['instance_port'] = raw_listener.get('InstancePort')
        listener_dict['load_balancer_port'] = raw_listener.get('LoadBalancerPort')
        listener_dict['protocol'] = raw_listener.get('Protocol')
        listener_dict['status'] = raw_listener.get('Status')
        listener_dict['band_width'] = raw_listener.get('Bandwidth')
        listener_dict['description'] = raw_listener.get('Description')
        
        port_id = f"{listener_dict['protocol']}-{listener_dict['load_balancer_port']}"
        return port_id, listener_dict
