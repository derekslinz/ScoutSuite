from aliyunsdkelasticsearch.request.v20170613 import ListInstancesRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ElasticsearchFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_instances(self, region):
        """
        Get all Elasticsearch instances

        :param region: region name
        :return: a list of instances
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListInstancesRequest.ListInstancesRequest()
        request.set_pageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Result', [])
        else:
            return []
