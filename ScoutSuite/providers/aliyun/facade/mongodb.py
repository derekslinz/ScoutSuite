from aliyunsdkmongodb.request.v20190802 import DescribeDBInstancesRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class MongoDBFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_instances(self, region):
        """
        Get all MongoDB instances

        :param region: region name
        :return: a list of instances
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('DBInstances', [])
        else:
            return []
