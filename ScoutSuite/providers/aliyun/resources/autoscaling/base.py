from ScoutSuite.providers.aliyun.resources.regions import Regions
from ScoutSuite.providers.aliyun.resources.autoscaling.scaling_groups import ScalingGroups
from ScoutSuite.providers.aliyun.resources.autoscaling.scaling_configurations import ScalingConfigurations
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class AutoScaling(Regions):
    _children = [
        (ScalingGroups, 'scaling_groups'),
        (ScalingConfigurations, 'scaling_configurations')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('autoscaling', facade)
