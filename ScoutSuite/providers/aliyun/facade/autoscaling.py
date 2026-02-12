from aliyunsdkess.request.v20140828 import DescribeScalingGroupsRequest, DescribeScalingConfigurationsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class AutoScalingFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_scaling_groups(self, region):
        """
        Get all auto scaling groups in a region

        :param region: region name
        :return: a list of all auto scaling groups
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeScalingGroupsRequest.DescribeScalingGroupsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('ScalingGroups', [])
        else:
            return []

    async def get_scaling_configurations(self, region):
        """
        Get all scaling configurations in a region

        :param region: region name
        :return: a list of all scaling configurations
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeScalingConfigurationsRequest.DescribeScalingConfigurationsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('ScalingConfigurations', [])
        else:
            return []
