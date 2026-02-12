from ScoutSuite.providers.aliyun.facade.base import AliyunFacade
from ScoutSuite.providers.base.services import BaseServicesConfig
from ScoutSuite.providers.aliyun.resources.ram.base import RAM
from ScoutSuite.providers.aliyun.resources.actiontrail.base import ActionTrail
from ScoutSuite.providers.aliyun.resources.vpc.base import VPC
from ScoutSuite.providers.aliyun.resources.ecs.base import ECS
from ScoutSuite.providers.aliyun.resources.rds.base import RDS
from ScoutSuite.providers.aliyun.resources.kms.base import KMS
from ScoutSuite.providers.aliyun.resources.oss.base import OSS
from ScoutSuite.providers.aliyun.resources.cdn.base import CDN
from ScoutSuite.providers.aliyun.resources.slb.base import SLB
from ScoutSuite.providers.aliyun.resources.autoscaling.base import AutoScaling
from ScoutSuite.providers.aliyun.resources.fc.base import FC
from ScoutSuite.providers.aliyun.resources.fnf.base import FNF
from ScoutSuite.providers.aliyun.resources.eventbridge.base import EventBridge
from ScoutSuite.providers.aliyun.resources.oos.base import OOS
from ScoutSuite.providers.aliyun.resources.ebs.base import EBS
from ScoutSuite.providers.aliyun.resources.sgw.base import SGW
from ScoutSuite.providers.aliyun.resources.hbr.base import HBR
from ScoutSuite.providers.aliyun.resources.dbs.base import DBS
from ScoutSuite.providers.aliyun.resources.smc.base import SMC
from ScoutSuite.providers.aliyun.resources.domain.base import Domain
from ScoutSuite.providers.aliyun.resources.elasticsearch.base import Elasticsearch
from ScoutSuite.providers.aliyun.resources.alidns.base import AliDNS
from ScoutSuite.providers.aliyun.resources.privatelink.base import Privatelink
from ScoutSuite.providers.aliyun.resources.sts.base import STS
from ScoutSuite.providers.aliyun.resources.vpcpeer.base import VPCPeer
from ScoutSuite.providers.aliyun.resources.das.base import DAS
from ScoutSuite.providers.aliyun.resources.adb.base import ADB
from ScoutSuite.providers.aliyun.resources.alikafka.base import AliKafka
from ScoutSuite.providers.aliyun.resources.mts.base import MTS
from ScoutSuite.providers.aliyun.resources.cloudsiem.base import CloudSIEM
from ScoutSuite.providers.aliyun.resources.arms.base import ARMS
from ScoutSuite.providers.aliyun.resources.cr.base import CR
from ScoutSuite.providers.aliyun.resources.dmsenterprises.base import DMSEnterprises
from ScoutSuite.providers.aliyun.resources.ack.base import ACK
from ScoutSuite.providers.aliyun.resources.api.base import API
from ScoutSuite.providers.aliyun.resources.mse.base import MSE
from ScoutSuite.providers.aliyun.resources.dds.base import DDS
from ScoutSuite.providers.aliyun.resources.kvstore.base import KVStore
from ScoutSuite.providers.aliyun.resources.maxcompute.base import MaxCompute
from ScoutSuite.providers.aliyun.resources.dataworks.base import DataWorks
from ScoutSuite.providers.aliyun.resources.expressconnect.base import ExpressConnect
from ScoutSuite.providers.aliyun.resources.acm.base import ACM
from ScoutSuite.providers.aliyun.resources.mongodb.base import MongoDB
from ScoutSuite.providers.aliyun.resources.sae.base import SAE
from ScoutSuite.providers.aliyun.resources.drds.base import DRDS
from ScoutSuite.providers.aliyun.resources.redis.base import Redis
from ScoutSuite.providers.aliyun.resources.memcache.base import Memcache
from ScoutSuite.providers.aliyun.resources.ots.base import OTS
from ScoutSuite.providers.aliyun.resources.log.base import Log
from ScoutSuite.providers.aliyun.resources.kafka.base import Kafka
from ScoutSuite.providers.aliyun.resources.rocketmq.base import RocketMQ
from ScoutSuite.providers.aliyun.resources.iot.base import IoT
from ScoutSuite.providers.aliyun.resources.polardbx.base import PolarDBX


class AliyunServicesConfig(BaseServicesConfig):
    def __init__(self, credentials, **kwargs):
        super().__init__(credentials)

        facade = AliyunFacade(credentials)

        self.actiontrail = ActionTrail(facade)
        self.ram = RAM(facade)
        self.ecs = ECS(facade)
        self.rds = RDS(facade)
        self.vpc = VPC(facade)
        self.kms = KMS(facade)
        self.oss = OSS(facade)
        self.cdn = CDN(facade)
        self.slb = SLB(facade)
        self.autoscaling = AutoScaling(facade)
        self.fc = FC(facade)
        self.fnf = FNF(facade)
        self.eventbridge = EventBridge(facade)
        self.oos = OOS(facade)
        self.ebs = EBS(facade)
        self.sgw = SGW(facade)
        self.hbr = HBR(facade)
        self.dbs = DBS(facade)
        self.smc = SMC(facade)
        self.domain = Domain(facade)
        self.elasticsearch = Elasticsearch(facade)
        self.alidns = AliDNS(facade)
        self.privatelink = Privatelink(facade)
        self.sts = STS(facade)
        self.vpcpeer = VPCPeer(facade)
        self.das = DAS(facade)
        self.adb = ADB(facade)
        self.alikafka = AliKafka(facade)
        self.mts = MTS(facade)
        self.cloudsiem = CloudSIEM(facade)
        self.arms = ARMS(facade)
        self.cr = CR(facade)
        self.dmsenterprises = DMSEnterprises(facade)
        self.ack = ACK(facade)
        self.api = API(facade)
        self.mse = MSE(facade)
        self.dds = DDS(facade)
        self.kvstore = KVStore(facade)
        self.maxcompute = MaxCompute(facade)
        self.dataworks = DataWorks(facade)
        self.expressconnect = ExpressConnect(facade)
        self.acm = ACM(facade)
        self.mongodb = MongoDB(facade)
        self.sae = SAE(facade)
        self.drds = DRDS(facade)
        self.redis = Redis(facade)
        self.memcache = Memcache(facade)
        self.ots = OTS(facade)
        self.log = Log(facade)
        self.kafka = Kafka(facade)
        self.rocketmq = RocketMQ(facade)
        self.iot = IoT(facade)
        self.polardbx = PolarDBX(facade)

    def _is_provider(self, provider_name):
        return provider_name == 'aliyun'
