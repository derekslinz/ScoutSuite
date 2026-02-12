from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class STSIdentity(AliyunResources):
    def __init__(self, identity_data):
        super().__init__('identity')
        self.extract_resources(identity_data)

    def extract_resources(self, identity_data):
        self['caller_identity'] = {
            'account_id': identity_data.get('AccountId'),
            'user_id': identity_data.get('UserId'),
            'arn': identity_data.get('Arn'),
            'identity_type': identity_data.get('IdentityType')
        }


class STS(AliyunCompositeResources):
    _children = [(STSIdentity, 'identity')]

    def __init__(self, facade):
        super().__init__('sts', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
