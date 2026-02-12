from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Domains(AliyunResources):
    def __init__(self, domains):
        super().__init__('domains')
        self.extract_resources(domains)

    def extract_resources(self, domains):
        for domain in domains:
            self[domain.get('DomainName')] = {
                'id': domain.get('DomainName'),
                'domain_name': domain.get('DomainName'),
                'registration_date': domain.get('RegistrationDate'),
                'expiration_date': domain.get('ExpirationDate'),
                'status': domain.get('DomainStatus'),
                'real_name_status': domain.get('Real-nameStatus')
            }


class Domain(Regions):
    _children = [(Domains, 'domains')]

    def __init__(self, facade):
        super().__init__('domain', facade)
