from aliyunsdkalikafka.request.v20190916 import GetInstanceListRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class AliKafkaFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_instances(self, region):
        """
        Get all Kafka instances

        :param region: region name
        :return: a list of instances
        """
        client = get_client(credentials=self._credentials, region=region)
        request = GetInstanceListRequest.GetInstanceListRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response.get('InstanceList', [])
        else:
            return []
