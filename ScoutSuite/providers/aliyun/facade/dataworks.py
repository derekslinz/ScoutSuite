from aliyunsdkdataworks.request.v20200518 import ListProjectsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class DataWorksFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_projects(self):
        """
        Get all DataWorks projects

        :return: a list of projects
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = ListProjectsRequest.ListProjectsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Projects', [])
        else:
            return []
