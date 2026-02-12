from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class ReplicationJobs(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_jobs = await self.facade.smc.get_replication_jobs()
        for raw_job in raw_jobs:
            id, job = await self._parse_job(raw_job)
            self[id] = job

    async def _parse_job(self, raw_job):
        job_dict = {}
        job_id = raw_job.get('JobId')
        
        job_dict['job_id'] = job_id
        job_dict['job_name'] = raw_job.get('JobName')
        job_dict['status'] = raw_job.get('Status')
        job_dict['source_id'] = raw_job.get('SourceId')
        job_dict['instance_id'] = raw_job.get('InstanceId')
        job_dict['instance_type'] = raw_job.get('InstanceType')
        job_dict['progress_percentage'] = raw_job.get('ProgressPercentage')
        job_dict['error_code'] = raw_job.get('ErrorCode')
        job_dict['error_message'] = raw_job.get('ErrorMessage')
        job_dict['create_time'] = raw_job.get('CreateTime')
        job_dict['start_time'] = raw_job.get('StartTime')
        job_dict['end_time'] = raw_job.get('EndTime')
        
        return job_id, job_dict
