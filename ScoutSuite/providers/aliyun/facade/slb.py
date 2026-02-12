from aliyunsdkslb.request.v20140515 import DescribeLoadBalancersRequest, DescribeListenersRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class SLBFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_load_balancers(self, region):
        """
        Get all load balancers in a region

        :param region: region name
        :return: a list of all load balancers
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeLoadBalancersRequest.DescribeLoadBalancersRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('LoadBalancers', [])
        else:
            return []

    async def get_listeners(self, region, load_balancer_id):
        """
        Get listeners for a load balancer

        :param region: region name
        :param load_balancer_id: load balancer ID
        :return: a list of listeners
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeListenersRequest.DescribeListenersRequest()
        request.set_LoadBalancerId(load_balancer_id)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Listeners', [])
        else:
            return []
