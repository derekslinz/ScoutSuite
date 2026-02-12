from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class PhysicalConnections(AliyunResources):
    def __init__(self, connections):
        super().__init__('physical_connections')
        self.extract_resources(connections)

    def extract_resources(self, connections):
        for connection in connections:
            self[connection.get('PhysicalConnectionId')] = {
                'id': connection.get('PhysicalConnectionId'),
                'physical_connection_id': connection.get('PhysicalConnectionId'),
                'name': connection.get('Name'),
                'status': connection.get('Status'),
                'circuit_code': connection.get('CircuitCode'),
                'bandwidth': connection.get('Bandwidth')
            }


class VirtualBorders(AliyunResources):
    def __init__(self, borders):
        super().__init__('virtual_borders')
        self.extract_resources(borders)

    def extract_resources(self, borders):
        for border in borders:
            self[border.get('VirtualBorderRouterId')] = {
                'id': border.get('VirtualBorderRouterId'),
                'virtual_border_router_id': border.get('VirtualBorderRouterId'),
                'name': border.get('Name'),
                'status': border.get('Status'),
                'vlan_id': border.get('VlanId')
            }


class ExpressConnect(Regions):
    _children = [(PhysicalConnections, 'physical_connections'), (VirtualBorders, 'virtual_borders')]

    def __init__(self, facade):
        super().__init__('expressconnect', facade)
