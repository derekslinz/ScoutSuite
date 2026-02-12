from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Instances(AliyunResources):
    def __init__(self, instances):
        super().__init__('instances')
        self.extract_resources(instances)

    def extract_resources(self, instances):
        for instance in instances:
            self[instance.get('InstanceId')] = {
                'id': instance.get('InstanceId'),
                'instance_id': instance.get('InstanceId'),
                'instance_name': instance.get('InstanceName'),
                'status': instance.get('StatusName'),
                'topic_count': instance.get('TopicCount'),
                'partition_count': instance.get('PartitionCount')
            }


class AliKafka(Regions):
    _children = [(Instances, 'instances')]

    def __init__(self, facade):
        super().__init__('alikafka', facade)
