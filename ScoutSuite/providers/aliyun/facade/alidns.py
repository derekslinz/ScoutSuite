from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class AliDNSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_domains(self):
        """
        Get all DNS domains

        :return: a list of domains
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = DescribeDomainsRequest.DescribeDomainsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Domains', {}).get('Domain', [])
        else:
            return []
