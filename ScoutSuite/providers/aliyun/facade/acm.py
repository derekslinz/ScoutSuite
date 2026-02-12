from aliyunsdkcas.request.v20200407 import ListUserCertificateRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ACMFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_certificates(self):
        """
        Get all SSL/TLS certificates

        :return: a list of certificates
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = ListUserCertificateRequest.ListUserCertificateRequest()
        request.set_ShowSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('CertificateList', [])
        else:
            return []
