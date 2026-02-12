from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Clusters(AliyunResources):
    def __init__(self, clusters):
        super().__init__('clusters')
        self.extract_resources(clusters)

    def extract_resources(self, clusters):
        for cluster in clusters:
            self[cluster.get('cluster_id')] = {
                'id': cluster.get('cluster_id'),
                'cluster_id': cluster.get('cluster_id'),
                'name': cluster.get('name'),
                'state': cluster.get('state'),
                'region_id': cluster.get('region_id'),
                'kubernetes_version': cluster.get('kubernetes_version')
            }


class ACK(Regions):
    _children = [(Clusters, 'clusters')]

    def __init__(self, facade):
        super().__init__('ack', facade)
