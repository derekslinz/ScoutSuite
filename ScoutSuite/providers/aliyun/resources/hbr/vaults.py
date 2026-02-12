from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Vaults(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_vaults = await self.facade.hbr.get_vaults()
        for raw_vault in raw_vaults:
            id, vault = await self._parse_vault(raw_vault)
            self[id] = vault

    async def _parse_vault(self, raw_vault):
        vault_dict = {}
        vault_id = raw_vault.get('VaultId')
        
        vault_dict['vault_id'] = vault_id
        vault_dict['vault_name'] = raw_vault.get('VaultName')
        vault_dict['vault_type'] = raw_vault.get('VaultType')
        vault_dict['region_id'] = raw_vault.get('RegionId')
        vault_dict['status'] = raw_vault.get('Status')
        vault_dict['created_at'] = raw_vault.get('CreatedTime')
        vault_dict['reason_code'] = raw_vault.get('ReasonCode')
        vault_dict['redundancy_type'] = raw_vault.get('RedundancyType')
        
        # Get detailed information
        details = await self.facade.hbr.get_vault(vault_id)
        if details:
            vault_dict['description'] = details.get('Description')
            vault_dict['encryption_key_id'] = details.get('EncryptionKeyId')
            vault_dict['kms_key_region'] = details.get('KmsKeyRegion')
            
        # Get backups
        backups = await self.facade.hbr.get_backups(vault_id)
        vault_dict['backup_count'] = len(backups)
        vault_dict['has_recent_backup'] = any(
            b.get('Status') == 'COMPLETED' for b in backups[-5:] if len(backups) >= 5
        ) if backups else False
        
        return vault_id, vault_dict
