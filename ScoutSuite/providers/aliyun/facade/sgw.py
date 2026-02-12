from aliyunsdksgw.request.v20180328 import ListGatewaysRequest, DescribeGatewayRequest, DescribeGatewayCachesRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class SGWFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_gateways(self, region='cn-shanghai'):
        """
        Get all Storage Gateway instances

        :param region: region name
        :return: a list of gateways
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListGatewaysRequest.ListGatewaysRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Gateways', [])
        else:
            return []

    async def get_gateway(self, gateway_id, region='cn-shanghai'):
        """
        Get Storage Gateway details

        :param gateway_id: gateway ID
        :param region: region name
        :return: gateway details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeGatewayRequest.DescribeGatewayRequest()
        request.set_GatewayId(gateway_id)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_gateway_caches(self, gateway_id, region='cn-shanghai'):
        """
        Get cache configuration for a gateway

        :param gateway_id: gateway ID
        :param region: region name
        :return: cache configuration
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeGatewayCachesRequest.DescribeGatewayCachesRequest()
        request.set_GatewayId(gateway_id)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('CacheConfigs', [])
        else:
            return []
