from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class EventBuses(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_buses = await self.facade.eventbridge.get_event_buses()
        for raw_bus in raw_buses:
            id, bus = await self._parse_event_bus(raw_bus)
            self[id] = bus

    async def _parse_event_bus(self, raw_bus):
        bus_dict = {}
        bus_name = raw_bus.get('Name')
        
        bus_dict['name'] = bus_name
        bus_dict['description'] = raw_bus.get('Description')
        bus_dict['arn'] = raw_bus.get('Arn')
        bus_dict['create_time'] = raw_bus.get('CreateTime')
        
        # Get detailed information
        details = await self.facade.eventbridge.get_event_bus(bus_name)
        if details:
            bus_dict['dlq_arn'] = details.get('DeadLetterQueueArn')
            
        # Get rules
        rules = await self.facade.eventbridge.get_rules(bus_name)
        bus_dict['rules'] = rules
        bus_dict['rule_count'] = len(rules)
        bus_dict['has_disabled_rules'] = any(
            not rule.get('State') or rule.get('State') != 'ENABLED'
            for rule in rules
        )
        
        return bus_name, bus_dict
