from aliyunsdksts.request.v20150401 import GetCallerIdentityRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class STSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_caller_identity(self):
        """
        Get caller identity information

        :return: caller identity details
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = GetCallerIdentityRequest.GetCallerIdentityRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response
        else:
            return {}
