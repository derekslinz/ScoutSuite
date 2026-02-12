from aliyunsdklog.request.v20201222 import ListProjectRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class LogFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_projects(self):
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = ListProjectRequest.ListProjectRequest()
        request.set_offset(0)
        request.set_size(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('projects', [])
        else:
            return []
