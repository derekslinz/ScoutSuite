from aliyunsdkmemcache.request.v20140815 import DescribeInstancesRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class MemcacheFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_instances(self, region):
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeInstancesRequest.DescribeInstancesRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Instances', [])
        else:
            return []
