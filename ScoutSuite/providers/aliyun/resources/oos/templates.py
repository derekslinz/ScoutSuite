from ScoutSuite.providers.aliyun.resources.base import AliyunResources
from ScoutSuite.providers.aliyun.facade.base import AliyunFacade


class Templates(AliyunResources):
    def __init__(self, facade: AliyunFacade):
        super().__init__(facade)

    async def fetch_all(self):
        raw_templates = await self.facade.oos.get_templates()
        for raw_template in raw_templates:
            id, template = await self._parse_template(raw_template)
            self[id] = template

    async def _parse_template(self, raw_template):
        template_dict = {}
        template_name = raw_template.get('TemplateName')
        
        template_dict['name'] = template_name
        template_dict['description'] = raw_template.get('Description')
        template_dict['template_type'] = raw_template.get('TemplateType')
        template_dict['version'] = raw_template.get('TemplateVersion')
        template_dict['created_date'] = raw_template.get('CreatedDate')
        template_dict['updated_date'] = raw_template.get('UpdatedDate')
        template_dict['owner'] = raw_template.get('Owner')
        
        # Get detailed information
        details = await self.facade.oos.get_template(template_name)
        if details:
            template_dict['content'] = details.get('Content')
            
        return template_name, template_dict
