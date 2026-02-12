from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class ScalingGroups(AliyunResources):
    def __init__(self, facade: AliyunFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        for raw_group in await self.facade.autoscaling.get_scaling_groups(region=self.region):
            id, group = await self._parse_scaling_group(raw_group)
            self[id] = group

    async def _parse_scaling_group(self, raw_group):
        group_dict = {}
        group_dict['scaling_group_id'] = raw_group.get('ScalingGroupId')
        group_dict['scaling_group_name'] = raw_group.get('ScalingGroupName')
        group_dict['scaling_configuration_id'] = raw_group.get('ScalingConfigurationId')
        group_dict['min_size'] = raw_group.get('MinSize')
        group_dict['max_size'] = raw_group.get('MaxSize')
        group_dict['desired_capacity'] = raw_group.get('DesiredCapacity')
        group_dict['health_check_type'] = raw_group.get('HealthCheckType')
        group_dict['load_balancer_ids'] = raw_group.get('LoadBalancerIds', [])
        group_dict['v_switch_ids'] = raw_group.get('VSwitchIds', [])
        group_dict['create_time'] = raw_group.get('CreateTime')
        group_dict['life_cycle_state'] = raw_group.get('LifecycleState')
        group_dict['tags'] = raw_group.get('Tags', {})
        group_dict['subnet_id'] = raw_group.get('SubnetId')
        group_dict['region_id'] = raw_group.get('RegionId')
        group_dict['enabled'] = raw_group.get('Enabled', True)
        
        return group_dict.get('scaling_group_id', 'unknown'), group_dict
