from aliyunsdkfc.request.v20160815 import ListServicesRequest, GetServiceRequest, ListFunctionsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class FCFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_services(self, region):
        """
        Get all Function Compute services

        :param region: region name
        :return: a list of services
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListServicesRequest.ListServicesRequest()
        request.set_Limit(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Services', [])
        else:
            return []

    async def get_service(self, service_name, region):
        """
        Get Function Compute service details

        :param service_name: service name
        :param region: region name
        :return: service details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = GetServiceRequest.GetServiceRequest()
        request.set_ServiceName(service_name)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_functions(self, service_name, region):
        """
        Get functions in a service

        :param service_name: service name
        :param region: region name
        :return: list of functions
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListFunctionsRequest.ListFunctionsRequest()
        request.set_ServiceName(service_name)
        request.set_Limit(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Functions', [])
        else:
            return []
