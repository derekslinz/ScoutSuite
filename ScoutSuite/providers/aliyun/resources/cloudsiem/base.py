from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class DataSources(AliyunResources):
    def __init__(self, sources):
        super().__init__('data_sources')
        self.extract_resources(sources)

    def extract_resources(self, sources):
        for source in sources:
            self[source.get('InstanceId')] = {
                'id': source.get('InstanceId'),
                'instance_id': source.get('InstanceId'),
                'instance_name': source.get('InstanceName'),
                'data_source_type': source.get('DataSourceType'),
                'account': source.get('Account')
            }


class CloudSIEM(AliyunCompositeResources):
    _children = [(DataSources, 'data_sources')]

    def __init__(self, facade):
        super().__init__('cloudsiem', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
