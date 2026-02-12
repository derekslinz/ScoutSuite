from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class PeeringConnections(AliyunResources):
    def __init__(self, connections):
        super().__init__('peering_connections')
        self.extract_resources(connections)

    def extract_resources(self, connections):
        for connection in connections:
            self[connection.get('PeeringConnectionId')] = {
                'id': connection.get('PeeringConnectionId'),
                'peering_connection_id': connection.get('PeeringConnectionId'),
                'local_vpc_id': connection.get('LocalVpcId'),
                'peer_vpc_id': connection.get('PeerVpcId'),
                'status': connection.get('Status'),
                'peering_type': connection.get('PeeringType')
            }


class VPCPeer(Regions):
    _children = [(PeeringConnections, 'peering_connections')]

    def __init__(self, facade):
        super().__init__('vpcpeer', facade)
