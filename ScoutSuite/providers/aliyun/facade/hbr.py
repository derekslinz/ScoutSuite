from aliyunsdkhbr.request.v20171218 import ListVaultsRequest, DescribeVaultRequest, ListBackupsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class HBRFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_vaults(self, region='cn-shanghai'):
        """
        Get all backup vaults

        :param region: region name
        :return: a list of vaults
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListVaultsRequest.ListVaultsRequest()
        request.set_Limit(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Vaults', [])
        else:
            return []

    async def get_vault(self, vault_id, region='cn-shanghai'):
        """
        Get vault details

        :param vault_id: vault ID
        :param region: region name
        :return: vault details
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeVaultRequest.DescribeVaultRequest()
        request.set_VaultId(vault_id)
        response = await get_response(client=client, request=request)
        return response if response else {}

    async def get_backups(self, vault_id, region='cn-shanghai'):
        """
        Get backups from a vault

        :param vault_id: vault ID
        :param region: region name
        :return: list of backups
        """
        client = get_client(credentials=self._credentials, region=region)
        request = ListBackupsRequest.ListBackupsRequest()
        request.set_VaultId(vault_id)
        request.set_Limit(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Backups', [])
        else:
            return []
