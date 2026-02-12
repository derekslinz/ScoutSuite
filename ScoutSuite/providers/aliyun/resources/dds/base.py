from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Instances(AliyunResources):
    def __init__(self, instances):
        super().__init__('instances')
        self.extract_resources(instances)

    def extract_resources(self, instances):
        for instance in instances:
            self[instance.get('DBInstanceId')] = {
                'id': instance.get('DBInstanceId'),
                'instance_id': instance.get('DBInstanceId'),
                'instance_name': instance.get('DBInstanceDescription'),
                'status': instance.get('DBInstanceStatus'),
                'engine': instance.get('Engine'),
                'engine_version': instance.get('EngineVersion')
            }


class DDS(Regions):
    _children = [(Instances, 'instances')]

    def __init__(self, facade):
        super().__init__('dds', facade)
