from aliyunsdksae.request.v20190111 import ListApplicationsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class SAEFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_applications(self, region):
        client = get_client(credentials=self._credentials, region=region)
        request = ListApplicationsRequest.ListApplicationsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Applications', [])
        else:
            return []
