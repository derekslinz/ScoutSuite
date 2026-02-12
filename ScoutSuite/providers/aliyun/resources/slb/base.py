from ScoutSuite.providers.aliyun.resources.regions import Regions
from ScoutSuite.providers.aliyun.resources.slb.load_balancers import LoadBalancers
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class SLB(Regions):
    _children = [
        (LoadBalancers, 'load_balancers')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('slb', facade)
