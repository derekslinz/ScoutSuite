from aliyunsdkmse.request.v20190531 import ListClustersRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class MSEFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_clusters(self, region):
        """
        Get all Microservices Engine clusters

        :param region: region name
        :return: a list of clusters
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListClustersRequest.ListClustersRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Clusters', [])
        else:
            return []
