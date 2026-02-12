from collections import Counter

from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver import LocalConfigRegionalEndpointResolver

from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.actiontrail import ActiontrailFacade
from ScoutSuite.providers.aliyun.facade.ecs import ECSFacade
from ScoutSuite.providers.aliyun.facade.kms import KMSFacade
from ScoutSuite.providers.aliyun.facade.ram import RAMFacade
from ScoutSuite.providers.aliyun.facade.rds import RDSFacade
from ScoutSuite.providers.aliyun.facade.vpc import VPCFacade
from ScoutSuite.providers.aliyun.facade.oss import OSSFacade
from ScoutSuite.providers.aliyun.facade.cdn import CDNFacade
from ScoutSuite.providers.aliyun.facade.slb import SLBFacade
from ScoutSuite.providers.aliyun.facade.autoscaling import AutoScalingFacade
from ScoutSuite.providers.aliyun.facade.fc import FCFacade
from ScoutSuite.providers.aliyun.facade.fnf import FNFFacade
from ScoutSuite.providers.aliyun.facade.eventbridge import EventBridgeFacade
from ScoutSuite.providers.aliyun.facade.oos import OOSFacade
from ScoutSuite.providers.aliyun.facade.ebs import EBSFacade
from ScoutSuite.providers.aliyun.facade.sgw import SGWFacade
from ScoutSuite.providers.aliyun.facade.hbr import HBRFacade
from ScoutSuite.providers.aliyun.facade.dbs import DBSFacade
from ScoutSuite.providers.aliyun.facade.smc import SMCFacade
from ScoutSuite.providers.aliyun.facade.domain import DomainFacade
from ScoutSuite.providers.aliyun.facade.elasticsearch import ElasticsearchFacade
from ScoutSuite.providers.aliyun.facade.alidns import AliDNSFacade
from ScoutSuite.providers.aliyun.facade.privatelink import PrivatelinkFacade
from ScoutSuite.providers.aliyun.facade.sts import STSFacade
from ScoutSuite.providers.aliyun.facade.vpcpeer import VPCPeerFacade
from ScoutSuite.providers.aliyun.facade.das import DASFacade
from ScoutSuite.providers.aliyun.facade.adb import ADBFacade
from ScoutSuite.providers.aliyun.facade.alikafka import AliKafkaFacade
from ScoutSuite.providers.aliyun.facade.mts import MTSFacade
from ScoutSuite.providers.aliyun.facade.cloudsiem import CloudSIEMFacade
from ScoutSuite.providers.aliyun.facade.arms import ARMSFacade
from ScoutSuite.providers.aliyun.facade.cr import CRFacade
from ScoutSuite.providers.aliyun.facade.dmsenterprises import DMSEnterpriseFacade
from ScoutSuite.providers.aliyun.facade.ack import ACKFacade
from ScoutSuite.providers.aliyun.facade.api import APIGatewayFacade
from ScoutSuite.providers.aliyun.facade.mse import MSEFacade
from ScoutSuite.providers.aliyun.facade.dds import DDSFacade
from ScoutSuite.providers.aliyun.facade.kvstore import KVStoreFacade
from ScoutSuite.providers.aliyun.facade.maxcompute import MaxComputeFacade
from ScoutSuite.providers.aliyun.facade.dataworks import DataWorksFacade
from ScoutSuite.providers.aliyun.facade.expressconnect import ExpressConnectFacade
from ScoutSuite.providers.aliyun.facade.acm import ACMFacade
from ScoutSuite.providers.aliyun.facade.mongodb import MongoDBFacade
from ScoutSuite.providers.aliyun.facade.sae import SAEFacade
from ScoutSuite.providers.aliyun.facade.drds import DRDSFacade
from ScoutSuite.providers.aliyun.facade.redis import RedisFacade
from ScoutSuite.providers.aliyun.facade.memcache import MemcacheFacade
from ScoutSuite.providers.aliyun.facade.ots import OTSFacade
from ScoutSuite.providers.aliyun.facade.log import LogFacade
from ScoutSuite.providers.aliyun.facade.kafka import KafkaFacade
from ScoutSuite.providers.aliyun.facade.rocketmq import RocketMQFacade
from ScoutSuite.providers.aliyun.facade.iot import IoTFacade
from ScoutSuite.providers.aliyun.facade.polardbx import PolarDBXFacade
from ScoutSuite.providers.utils import run_concurrently


class AliyunFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials
        self._instantiate_facades()
        self._resolver = LocalConfigRegionalEndpointResolver()

    def _instantiate_facades(self):
        self.actiontrail = ActiontrailFacade(self._credentials)
        self.ram = RAMFacade(self._credentials)
        self.ecs = ECSFacade(self._credentials)
        self.rds = RDSFacade(self._credentials)
        self.vpc = VPCFacade(self._credentials)
        self.kms = KMSFacade(self._credentials)
        self.oss = OSSFacade(self._credentials)
        self.cdn = CDNFacade(self._credentials)
        self.slb = SLBFacade(self._credentials)
        self.autoscaling = AutoScalingFacade(self._credentials)
        self.fc = FCFacade(self._credentials)
        self.fnf = FNFFacade(self._credentials)
        self.eventbridge = EventBridgeFacade(self._credentials)
        self.oos = OOSFacade(self._credentials)
        self.ebs = EBSFacade(self._credentials)
        self.sgw = SGWFacade(self._credentials)
        self.hbr = HBRFacade(self._credentials)
        self.dbs = DBSFacade(self._credentials)
        self.smc = SMCFacade(self._credentials)
        self.domain = DomainFacade(self._credentials)
        self.elasticsearch = ElasticsearchFacade(self._credentials)
        self.alidns = AliDNSFacade(self._credentials)
        self.privatelink = PrivatelinkFacade(self._credentials)
        self.sts = STSFacade(self._credentials)
        self.vpcpeer = VPCPeerFacade(self._credentials)
        self.das = DASFacade(self._credentials)
        self.adb = ADBFacade(self._credentials)
        self.alikafka = AliKafkaFacade(self._credentials)
        self.mts = MTSFacade(self._credentials)
        self.cloudsiem = CloudSIEMFacade(self._credentials)
        self.arms = ARMSFacade(self._credentials)
        self.cr = CRFacade(self._credentials)
        self.dmsenterprises = DMSEnterpriseFacade(self._credentials)
        self.ack = ACKFacade(self._credentials)
        self.api = APIGatewayFacade(self._credentials)
        self.mse = MSEFacade(self._credentials)
        self.dds = DDSFacade(self._credentials)
        self.kvstore = KVStoreFacade(self._credentials)
        self.maxcompute = MaxComputeFacade(self._credentials)
        self.dataworks = DataWorksFacade(self._credentials)
        self.expressconnect = ExpressConnectFacade(self._credentials)
        self.acm = ACMFacade(self._credentials)
        self.mongodb = MongoDBFacade(self._credentials)
        self.sae = SAEFacade(self._credentials)
        self.drds = DRDSFacade(self._credentials)
        self.redis = RedisFacade(self._credentials)
        self.memcache = MemcacheFacade(self._credentials)
        self.ots = OTSFacade(self._credentials)
        self.log = LogFacade(self._credentials)
        self.kafka = KafkaFacade(self._credentials)
        self.rocketmq = RocketMQFacade(self._credentials)
        self.iot = IoTFacade(self._credentials)
        self.polardbx = PolarDBXFacade(self._credentials)

    async def build_region_list(self, service: str, chosen_regions=None):

        # TODO could need this for service ids
        # service = 'ec2containerservice' if service == 'ecs' else service

        # TODO does a similar endpoint exist?
        # available_services = await run_concurrently(lambda: Session().get_available_services())
        # if service not in available_services:
        #     raise Exception('Service ' + service + ' is not available.')

        regions = await run_concurrently(
            lambda: self._resolver.get_valid_region_ids_by_product(product_code=service))

        if chosen_regions:
            return list((Counter(regions) & Counter(chosen_regions)).elements())
        else:
            return regions
