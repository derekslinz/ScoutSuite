from aliyunsdkcr.request.v20181201 import GetRepositoryListRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class CRFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_repositories(self):
        """
        Get all container repositories

        :return: a list of repositories
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = GetRepositoryListRequest.GetRepositoryListRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Repositories', [])
        else:
            return []
