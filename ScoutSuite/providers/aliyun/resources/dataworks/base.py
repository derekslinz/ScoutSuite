from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class Projects(AliyunResources):
    def __init__(self, projects):
        super().__init__('projects')
        self.extract_resources(projects)

    def extract_resources(self, projects):
        for project in projects:
            self[project.get('ProjectId')] = {
                'id': project.get('ProjectId'),
                'project_id': project.get('ProjectId'),
                'project_name': project.get('ProjectName'),
                'description': project.get('Description')
            }


class DataWorks(AliyunCompositeResources):
    _children = [(Projects, 'projects')]

    def __init__(self, facade):
        super().__init__('dataworks', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
