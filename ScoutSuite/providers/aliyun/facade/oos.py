from aliyunsdkoos.request.v20160815 import ListTemplatesRequest, GetTemplateRequest, ListTasksRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class OOSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_templates(self, region='cn-shanghai'):
        """
        Get all CloudOps templates

        :param region: region name
        :return: a list of templates
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListTemplatesRequest.ListTemplatesRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Templates', [])
        else:
            return []

    async def get_template(self, template_name, region='cn-shanghai'):
        """
        Get CloudOps template details

        :param template_name: template name
        :param region: region name
        :return: template details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = GetTemplateRequest.GetTemplateRequest()
        request.set_TemplateName(template_name)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_tasks(self, region='cn-shanghai'):
        """
        Get all CloudOps tasks

        :param region: region name
        :return: a list of tasks
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListTasksRequest.ListTasksRequest()
        request.set_MaxSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Tasks', [])
        else:
            return []
