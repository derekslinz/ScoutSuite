from aliyunsdkcloudsiem.request.v20220616 import DescribeDataSourceInstanceRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class CloudSIEMFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_data_sources(self):
        """
        Get all CloudSIEM data sources

        :return: a list of data sources
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = DescribeDataSourceInstanceRequest.DescribeDataSourceInstanceRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Data', [])
        else:
            return []
