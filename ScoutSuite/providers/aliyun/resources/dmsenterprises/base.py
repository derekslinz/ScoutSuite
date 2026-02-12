from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class MigrationJobs(AliyunResources):
    def __init__(self, jobs):
        super().__init__('migration_jobs')
        self.extract_resources(jobs)

    def extract_resources(self, jobs):
        for job in jobs:
            self[job.get('MigrationJobId')] = {
                'id': job.get('MigrationJobId'),
                'migration_job_id': job.get('MigrationJobId'),
                'migration_job_name': job.get('MigrationJobName'),
                'status': job.get('MigrationJobStatus'),
                'source_endpoint': job.get('SourceEndpoint'),
                'destination_endpoint': job.get('DestinationEndpoint')
            }


class DMSEnterprises(AliyunCompositeResources):
    _children = [(MigrationJobs, 'migration_jobs')]

    def __init__(self, facade):
        super().__init__('dmsenterprises', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
