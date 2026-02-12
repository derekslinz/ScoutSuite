from aliyunsdkfnf.request.v20190315 import ListFlowsRequest, DescribeFlowRequest, GetExecutionHistoryRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class FNFFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_flows(self, region='cn-shanghai'):
        """
        Get all CloudFlow workflows

        :param region: region name
        :return: a list of workflows
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListFlowsRequest.ListFlowsRequest()
        request.set_Limit(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Flows', [])
        else:
            return []

    async def get_flow(self, flow_name, region='cn-shanghai'):
        """
        Get CloudFlow workflow details

        :param flow_name: workflow name
        :param region: region name
        :return: workflow details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeFlowRequest.DescribeFlowRequest()
        request.set_Name(flow_name)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_execution_history(self, flow_name, region='cn-shanghai'):
        """
        Get execution history for a workflow

        :param flow_name: workflow name
        :param region: region name
        :return: execution history
        """
        client = get_client(credentials=self._credentials, region=region)
        request = GetExecutionHistoryRequest.GetExecutionHistoryRequest()
        request.set_FlowName(flow_name)
        request.set_Limit(10)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Executions', [])
        else:
            return []
