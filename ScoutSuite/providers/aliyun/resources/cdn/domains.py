from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Domains(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        for raw_domain in await self.facade.cdn.get_domains():
            id, domain = await self._parse_domain(raw_domain)
            self[id] = domain

    async def _parse_domain(self, raw_domain):
        domain_dict = {}
        domain_dict['domain_name'] = raw_domain.get('DomainName', '')
        domain_dict['cname'] = raw_domain.get('Cname', '')
        domain_dict['status'] = raw_domain.get('Status', '')
        domain_dict['create_time'] = raw_domain.get('CreateTime', '')
        domain_dict['update_time'] = raw_domain.get('UpdateTime', '')
        domain_dict['scope'] = raw_domain.get('Scope', '')
        domain_dict['cdn_type'] = raw_domain.get('CdnType', '')
        domain_dict['description'] = raw_domain.get('Description', '')
        domain_dict['ssl_protocol'] = raw_domain.get('SslProtocol', '')
        domain_dict['ssl_pub'] = raw_domain.get('SslPub', '')
        
        return domain_dict.get('domain_name', 'unknown'), domain_dict
