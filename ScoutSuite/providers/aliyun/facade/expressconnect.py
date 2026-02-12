from aliyunsdkexpressconnect.request.v20160930 import DescribePhysicalConnectionsRequest, DescribeVirtualBordersRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ExpressConnectFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_physical_connections(self, region):
        """
        Get all physical connections

        :param region: region name
        :return: a list of connections
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribePhysicalConnectionsRequest.DescribePhysicalConnectionsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('PhysicalConnectionSet', [])
        else:
            return []

    async def get_virtual_borders(self, region):
        """
        Get all virtual borders

        :param region: region name
        :return: a list of virtual borders
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeVirtualBordersRequest.DescribeVirtualBordersRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('VirtualBorderSet', [])
        else:
            return []
