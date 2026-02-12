from aliyunsdkmts.request.v20140618 import ListPipelineRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class MTSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_pipelines(self, region):
        """
        Get all media transcoding pipelines

        :param region: region name
        :return: a list of pipelines
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListPipelineRequest.ListPipelineRequest()
        response = await get_response(client=client, request=request)
        if response:
            return response.get('PipelineList', [])
        else:
            return []
