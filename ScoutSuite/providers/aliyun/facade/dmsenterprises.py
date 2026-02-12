from aliyunsdkdts.request.v20200101 import DescribeMigrationJobsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class DMSEnterpriseFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_migration_jobs(self):
        """
        Get all DMS migration jobs

        :return: a list of migration jobs
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = DescribeMigrationJobsRequest.DescribeMigrationJobsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('MigrationJobs', [])
        else:
            return []
