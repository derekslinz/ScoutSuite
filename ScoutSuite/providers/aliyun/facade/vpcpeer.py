from aliyunsdkvpcpeer.request.v20220901 import ListPeeringConnectionsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class VPCPeerFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_peering_connections(self, region):
        """
        Get all VPC peering connections

        :param region: region name
        :return: a list of peering connections
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListPeeringConnectionsRequest.ListPeeringConnectionsRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('PeeringConnections', [])
        else:
            return []
