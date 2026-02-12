from aliyunsdkeventbridge.request.v20200401 import ListEventBusesRequest, GetEventBusRequest, ListRulesRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class EventBridgeFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_event_buses(self, region='cn-shanghai'):
        """
        Get all event buses

        :param region: region name
        :return: a list of event buses
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListEventBusesRequest.ListEventBusesRequest()
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('EventBuses', [])
        else:
            return []

    async def get_event_bus(self, event_bus_name, region='cn-shanghai'):
        """
        Get event bus details

        :param event_bus_name: event bus name
        :param region: region name
        :return: event bus details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = GetEventBusRequest.GetEventBusRequest()
        request.set_EventBusName(event_bus_name)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_rules(self, event_bus_name, region='cn-shanghai'):
        """
        Get rules for an event bus

        :param event_bus_name: event bus name
        :param region: region name
        :return: list of rules
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListRulesRequest.ListRulesRequest()
        request.set_EventBusName(event_bus_name)
        request.set_MaxResults(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Rules', [])
        else:
            return []
