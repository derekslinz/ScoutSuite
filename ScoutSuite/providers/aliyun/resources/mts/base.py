from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Pipelines(AliyunResources):
    def __init__(self, pipelines):
        super().__init__('pipelines')
        self.extract_resources(pipelines)

    def extract_resources(self, pipelines):
        for pipeline in pipelines:
            self[pipeline.get('Id')] = {
                'id': pipeline.get('Id'),
                'pipeline_id': pipeline.get('Id'),
                'name': pipeline.get('Name'),
                'state': pipeline.get('State'),
                'notify_topic_arn': pipeline.get('NotifyTopicArn')
            }


class MTS(Regions):
    _children = [(Pipelines, 'pipelines')]

    def __init__(self, facade):
        super().__init__('mts', facade)
