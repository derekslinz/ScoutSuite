from aliyunsdkdomain.request.v20180129 import QueryDomainListRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class DomainFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_domains(self, region):
        """
        Get all registered domains

        :param region: region name
        :return: a list of domains
        """
        client = get_client(credentials=self._credentials, region=region)
        request = QueryDomainListRequest.QueryDomainListRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Data', [])
        else:
            return []
