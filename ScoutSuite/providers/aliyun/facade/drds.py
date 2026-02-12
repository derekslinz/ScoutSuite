from aliyunsdkdrds.request.v20180327 import DescribeDrdsInstanceRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class DRDSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_instances(self, region):
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeDrdsInstanceRequest.DescribeDrdsInstanceRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Data', [])
        else:
            return []
