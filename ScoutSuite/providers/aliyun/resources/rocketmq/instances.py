from ScoutSuite.providers.aliyun.resources.base import AliyunResources


class Instances(AliyunResources):
    multiple = 'instances'
    singular = 'instance'
    flagged_keys = AliyunResources.flagged_keys + ['InstanceDescription']
