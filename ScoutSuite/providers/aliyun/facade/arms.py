from aliyunsdkarms.request.v20190808 import ListPrometheusRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class ARMSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_monitoring_instances(self):
        """
        Get all ARMS monitoring instances

        :return: a list of monitoring instances
        """
        client = get_client(credentials=self._credentials, region='cn-hangzhou')
        request = ListPrometheusRequest.ListPrometheusRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('PrometheusInstances', [])
        else:
            return []
