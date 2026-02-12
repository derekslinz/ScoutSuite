from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Disks(AliyunCompositeResources):
    def __init__(self, facade: AliyunFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        raw_disks = await self.facade.ebs.get_disks(self.region)
        for raw_disk in raw_disks:
            id, disk = await self._parse_disk(raw_disk)
            self[id] = disk

    async def _parse_disk(self, raw_disk):
        disk_dict = {}
        disk_id = raw_disk.get('DiskId')
        
        disk_dict['id'] = disk_id
        disk_dict['disk_id'] = disk_id
        disk_dict['zone_id'] = raw_disk.get('ZoneId')
        disk_dict['disk_name'] = raw_disk.get('DiskName')
        disk_dict['description'] = raw_disk.get('Description')
        disk_dict['region_id'] = raw_disk.get('RegionId')
        disk_dict['size'] = raw_disk.get('Size')
        disk_dict['type'] = raw_disk.get('Type')
        disk_dict['category'] = raw_disk.get('Category')
        disk_dict['status'] = raw_disk.get('Status')
        disk_dict['created_at'] = raw_disk.get('CreationTime')
        disk_dict['encrypted'] = raw_disk.get('Encrypted')
        disk_dict['kms_key_id'] = raw_disk.get('KmsKeyId')
        disk_dict['delete_with_instance'] = raw_disk.get('DeleteWithInstance')
        
        return disk_id, disk_dict
