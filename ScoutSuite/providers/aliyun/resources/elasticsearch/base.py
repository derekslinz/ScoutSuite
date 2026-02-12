from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Instances(AliyunResources):
    def __init__(self, instances):
        super().__init__('instances')
        self.extract_resources(instances)

    def extract_resources(self, instances):
        for instance in instances:
            self[instance.get('instanceId')] = {
                'id': instance.get('instanceId'),
                'instance_id': instance.get('instanceId'),
                'name': instance.get('instanceName'),
                'status': instance.get('instanceStatus'),
                'region': instance.get('regionId'),
                'version': instance.get('esVersion'),
                'data_node_amount': instance.get('nodeAmount'),
                'subscription_type': instance.get('paymentType')
            }


class Elasticsearch(Regions):
    _children = [(Instances, 'instances')]

    def __init__(self, facade):
        super().__init__('elasticsearch', facade)
