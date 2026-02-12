from aliyunsdkacs.request.v20170616 import ListClustersRequest, DescribeClusterDetailRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ACKFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_clusters(self, region):
        """
        Get all Kubernetes clusters

        :param region: region name
        :return: a list of clusters
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListClustersRequest.ListClustersRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response.get('clusters', [])
        else:
            return []

    async def get_cluster_detail(self, region, cluster_id):
        """
        Get cluster details

        :param region: region name
        :param cluster_id: cluster ID
        :return: cluster details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeClusterDetailRequest.DescribeClusterDetailRequest()
        request.set_ClusterId(cluster_id)
        response = await get_response(client=client, request=request)
        if response:
            return response
        else:
            return {}
