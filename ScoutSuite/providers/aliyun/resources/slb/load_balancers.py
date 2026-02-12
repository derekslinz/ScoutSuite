from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.slb.listeners import Listeners
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class LoadBalancers(AliyunResources):
    def __init__(self, facade: AliyunFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        for raw_lb in await self.facade.slb.get_load_balancers(region=self.region):
            id, lb = await self._parse_load_balancer(raw_lb)
            self[id] = lb

    async def _parse_load_balancer(self, raw_lb):
        lb_dict = {}
        lb_dict['load_balancer_id'] = raw_lb.get('LoadBalancerId')
        lb_dict['load_balancer_name'] = raw_lb.get('LoadBalancerName')
        lb_dict['status'] = raw_lb.get('Status')
        lb_dict['address'] = raw_lb.get('Address')
        lb_dict['address_type'] = raw_lb.get('AddressType')
        lb_dict['create_time'] = raw_lb.get('CreateTime')
        lb_dict['region_id'] = raw_lb.get('RegionId')
        lb_dict['internet_charge_type'] = raw_lb.get('InternetChargeType')
        lb_dict['band_width'] = raw_lb.get('Bandwidth')
        lb_dict['vpc_id'] = raw_lb.get('VpcId')
        lb_dict['network_type'] = raw_lb.get('NetworkType')
        lb_dict['tags'] = raw_lb.get('Tags', {})
        lb_dict['listeners'] = {}
        
        # Fetch listeners for this load balancer
        listeners_obj = Listeners(self.facade, self.region, lb_dict['load_balancer_id'])
        await listeners_obj.fetch_all()
        lb_dict['listeners'] = dict(listeners_obj)
        
        return lb_dict.get('load_balancer_id', 'unknown'), lb_dict
