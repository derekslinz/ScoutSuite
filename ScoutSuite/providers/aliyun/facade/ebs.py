from aliyunsdkebs.request.v20160328 import DescribeDisksRequest, DescribeSnapshotsRequest
from ScoutSuite.providers.aliyun.utils import get_client
from ScoutSuite.providers.aliyun.authentication_strategy import AliyunCredentials
from ScoutSuite.providers.aliyun.facade.utils import get_response


class EBSFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials

    async def get_disks(self, region):
        """
        Get all elastic block storage disks

        :param region: region name
        :return: a list of disks
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeDisksRequest.DescribeDisksRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Disks', [])
        else:
            return []

    async def get_snapshots(self, region):
        """
        Get all disk snapshots

        :param region: region name
        :return: a list of snapshots
        """
        client = get_client(credentials=self._credentials, region=region)
        request = DescribeSnapshotsRequest.DescribeSnapshotsRequest()
        request.set_PageSize(100)
        response = await get_response(client=client, request=request)
        if response:
            return response.get('Snapshots', [])
        else:
            return []
