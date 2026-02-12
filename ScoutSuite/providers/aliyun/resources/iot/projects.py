from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources


class Projects(AliyunCompositeResources):
    multiple = 'projects'
    singular = 'project'
    flagged_keys = AliyunCompositeResources.flagged_keys + ['ProjectDescription']

    async def fetch_all(self):
        self.resources = {}
        projects = await self.facade.get_projects()
        for project in projects:
            self.resources[project.get('projectId')] = project
