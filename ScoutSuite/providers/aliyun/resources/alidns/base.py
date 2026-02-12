from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class Domains(AliyunResources):
    def __init__(self, domains):
        super().__init__('domains')
        self.extract_resources(domains)

    def extract_resources(self, domains):
        for domain in domains:
            self[domain.get('DomainId')] = {
                'id': domain.get('DomainId'),
                'domain_name': domain.get('DomainName'),
                'group_id': domain.get('GroupId'),
                'group_name': domain.get('GroupName'),
                'punycode': domain.get('Punycode'),
                'ali_domain': domain.get('AliDomain')
            }


class AliDNS(AliyunCompositeResources):
    _children = [(Domains, 'domains')]

    def __init__(self, facade):
        super().__init__('alidns', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
