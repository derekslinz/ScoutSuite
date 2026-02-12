from aliyunsdkprivatelink.request.v20200415 import ListVpcEndpointServicesRequest, ListVpcEndpointsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class PrivatelinkFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_vpc_endpoint_services(self, region):
        """
        Get all VPC endpoint services

        :param region: region name
        :return: a list of endpoint services
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListVpcEndpointServicesRequest.ListVpcEndpointServicesRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Services', [])
        else:
            return []

    async def get_vpc_endpoints(self, region):
        """
        Get all VPC endpoints

        :param region: region name
        :return: a list of endpoints
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListVpcEndpointsRequest.ListVpcEndpointsRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Endpoints', [])
        else:
            return []
