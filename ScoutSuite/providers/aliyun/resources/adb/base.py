from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.resources.regions import Regions


class Clusters(AliyunResources):
    def __init__(self, clusters):
        super().__init__('clusters')
        self.extract_resources(clusters)

    def extract_resources(self, clusters):
        for cluster in clusters:
            self[cluster.get('DBClusterId')] = {
                'id': cluster.get('DBClusterId'),
                'db_cluster_id': cluster.get('DBClusterId'),
                'db_cluster_description': cluster.get('DBClusterDescription'),
                'db_cluster_status': cluster.get('DBClusterStatus'),
                'db_type': cluster.get('DBType'),
                'db_version': cluster.get('DBVersion'),
                'region': cluster.get('RegionId')
            }


class ADB(Regions):
    _children = [(Clusters, 'clusters')]

    def __init__(self, facade):
        super().__init__('adb', facade)
