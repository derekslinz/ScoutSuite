from aliyunsdksmc.request.v20190601 import DescribeSourceServersRequest, DescribeReplicationJobsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class SMCFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_source_servers(self, region='cn-shanghai'):
        """
        Get all source servers for migration

        :param region: region name
        :return: a list of source servers
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeSourceServersRequest.DescribeSourceServersRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('SourceServers', [])
        else:
            return []

    async def get_replication_jobs(self, region='cn-shanghai'):
        """
        Get all replication jobs

        :param region: region name
        :return: a list of replication jobs
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeReplicationJobsRequest.DescribeReplicationJobsRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('ReplicationJobs', [])
        else:
            return []
