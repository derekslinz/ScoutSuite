from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Apis(AliyunResources):
    def __init__(self, apis):
        super().__init__('apis')
        self.extract_resources(apis)

    def extract_resources(self, apis):
        for api in apis:
            self[api.get('ApiId')] = {
                'id': api.get('ApiId'),
                'api_id': api.get('ApiId'),
                'api_name': api.get('ApiName'),
                'api_path': api.get('ApiPath'),
                'http_method': api.get('HttpMethod'),
                'visibility': api.get('Visibility')
            }


class API(Regions):
    _children = [(Apis, 'apis')]

    def __init__(self, facade):
        super().__init__('api', facade)
