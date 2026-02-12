from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions
from ScoutSuite.providers.aliyun.resources.ebs.disks import Disks


class EBS(Regions):
    _children = [(Disks, 'disks')]

    def __init__(self, facade):
        super().__init__('ebs', facade)
