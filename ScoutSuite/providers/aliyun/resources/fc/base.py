from ScoutSuite.providers.aliyun.resources.regions import Regions
from ScoutSuite.providers.aliyun.resources.fc.services import Services


class FC(Regions):
    _children = [(Services, 'services')]

    def __init__(self, facade):
        super().__init__('fc', facade)
