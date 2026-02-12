from aliyunsdkdbs.request.v20190101 import DescribeBackupPlanListRequest, DescribeRestorePlanListRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class DBSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_backup_plans(self, region='cn-shanghai'):
        """
        Get all database backup plans

        :param region: region name
        :return: a list of backup plans
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeBackupPlanListRequest.DescribeBackupPlanListRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Items', [])
        else:
            return []

    async def get_restore_plans(self, region='cn-shanghai'):
        """
        Get all database restore plans

        :param region: region name
        :return: a list of restore plans
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeRestorePlanListRequest.DescribeRestorePlanListRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Items', [])
        else:
            return []
