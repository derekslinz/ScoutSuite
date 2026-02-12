from aliyunsdkcdn.request.v20180510 import DescribeUserDomainsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class CDNFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_domains(self):
        """
        Get all CDN domains

        :return: a list of all CDN domains
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = DescribeUserDomainsRequest.DescribeUserDomainsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Domains', {}).get('PageData', [])
        else:
            return []
