from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Clusters(AliyunResources):
    def __init__(self, clusters):
        super().__init__('clusters')
        self.extract_resources(clusters)

    def extract_resources(self, clusters):
        for cluster in clusters:
            self[cluster.get('ClusterId')] = {
                'id': cluster.get('ClusterId'),
                'cluster_id': cluster.get('ClusterId'),
                'cluster_name': cluster.get('ClusterName'),
                'cluster_type': cluster.get('ClusterType'),
                'status': cluster.get('Status')
            }


class MSE(Regions):
    _children = [(Clusters, 'clusters')]

    def __init__(self, facade):
        super().__init__('mse', facade)
