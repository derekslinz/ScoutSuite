from aliyunsdkadb.request.v20211126 import DescribeDBClustersRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ADBFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_clusters(self, region):
        """
        Get all Analytics Database clusters

        :param region: region name
        :return: a list of clusters
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeDBClustersRequest.DescribeDBClustersRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Items', [])
        else:
            return []
