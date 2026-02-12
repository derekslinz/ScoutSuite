from ScoutSuite.providers.aliyun.resources.base import AliyunCompositeResources, AliyunResources


class Repositories(AliyunResources):
    def __init__(self, repositories):
        super().__init__('repositories')
        self.extract_resources(repositories)

    def extract_resources(self, repositories):
        for repo in repositories:
            self[repo.get('RepoId')] = {
                'id': repo.get('RepoId'),
                'repo_id': repo.get('RepoId'),
                'repo_name': repo.get('RepoName'),
                'repo_namespace': repo.get('RepoNamespace'),
                'repo_type': repo.get('RepoType'),
                'summary': repo.get('Summary')
            }


class CR(AliyunCompositeResources):
    _children = [(Repositories, 'repositories')]

    def __init__(self, facade):
        super().__init__('cr', facade)

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
