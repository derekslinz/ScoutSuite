from aliyunsdkapigateway.request.v20160408 import DescribeApisRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class APIGatewayFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_apis(self, region):
        """
        Get all APIs

        :param region: region name
        :return: a list of APIs
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeApisRequest.DescribeApisRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('ApiSummarys', [])
        else:
            return []
