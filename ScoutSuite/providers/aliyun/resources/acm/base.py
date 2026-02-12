from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class Certificates(AliyunResources):
    def __init__(self, certificates):
        super().__init__('certificates')
        self.extract_resources(certificates)

    def extract_resources(self, certificates):
        for cert in certificates:
            self[cert.get('CertId')] = {
                'id': cert.get('CertId'),
                'cert_id': cert.get('CertId'),
                'cert_name': cert.get('CertName'),
                'certificate_type': cert.get('CertType'),
                'expired': cert.get('Expired'),
                'expire_time': cert.get('ExpireTime')
            }


class ACM(AliyunCompositeResources):
    _children = [(Certificates, 'certificates')]

    def __init__(self, facade):
        super().__init__('acm', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
