from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class MonitoringInstances(AliyunResources):
    def __init__(self, instances):
        super().__init__('monitoring_instances')
        self.extract_resources(instances)

    def extract_resources(self, instances):
        for instance in instances:
            self[instance.get('InstanceId')] = {
                'id': instance.get('InstanceId'),
                'instance_id': instance.get('InstanceId'),
                'instance_name': instance.get('InstanceName'),
                'instance_alias': instance.get('InstanceAlias'),
                'type': instance.get('Type'),
                'gmt_create': instance.get('GmtCreate')
            }


class ARMS(AliyunCompositeResources):
    _children = [(MonitoringInstances, 'monitoring_instances')]

    def __init__(self, facade):
        super().__init__('arms', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
