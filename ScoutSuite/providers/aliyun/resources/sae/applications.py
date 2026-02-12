from ScoutSuite.providers.aliyun.resources.base import AliyunResources


class Applications(AliyunResources):
    multiple = 'applications'
    singular = 'application'
    flagged_keys = AliyunResources.flagged_keys + ['AppDescription']
