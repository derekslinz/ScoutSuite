from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class ScalingConfigurations(AliyunResources):
    def __init__(self, facade: AliyunFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        for raw_config in await self.facade.autoscaling.get_scaling_configurations(region=self.region):
            id, config = await self._parse_scaling_configuration(raw_config)
            self[id] = config

    async def _parse_scaling_configuration(self, raw_config):
        config_dict = {}
        config_dict['scaling_configuration_id'] = raw_config.get('ScalingConfigurationId')
        config_dict['scaling_configuration_name'] = raw_config.get('ScalingConfigurationName')
        config_dict['image_id'] = raw_config.get('ImageId')
        config_dict['instance_type'] = raw_config.get('InstanceType')
        config_dict['instance_types'] = raw_config.get('InstanceTypes', [])
        config_dict['key_pair_name'] = raw_config.get('KeyPairName')
        config_dict['security_group_id'] = raw_config.get('SecurityGroupId')
        config_dict['create_time'] = raw_config.get('CreateTime')
        config_dict['lifecycle_state'] = raw_config.get('LifecycleState')
        config_dict['user_data'] = raw_config.get('UserData')
        config_dict['spot_price_limit'] = raw_config.get('SpotPriceLimit')
        config_dict['spot_strategy'] = raw_config.get('SpotStrategy')
        
        return config_dict.get('scaling_configuration_id', 'unknown'), config_dict
