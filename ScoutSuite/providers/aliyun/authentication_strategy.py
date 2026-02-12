import json
import os
from getpass import getpass

from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.client import AcsClient
from aliyunsdksts.request.v20150401 import GetCallerIdentityRequest

from ScoutSuite.providers.base.authentication_strategy import AuthenticationStrategy, AuthenticationException


class AliyunCredentials:

    def __init__(self, credentials, caller_details):
        self.credentials = credentials
        self.caller_details = caller_details


class AliyunAuthenticationStrategy(AuthenticationStrategy):
    """
    Implements authentication for the Aliyun provider
    """

    @staticmethod
    def _get_profile_credentials(profile=None):
        config_file = os.path.expanduser('~/.aliyun/config.json')
        if not os.path.exists(config_file):
            return (None, None)

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception:
            return (None, None)

        profiles = config.get('profiles') or []
        if isinstance(profiles, dict):
            profiles = [profiles]

        # If profile is not provided, use the current profile then fallback to "default".
        profile_name = profile or config.get('current') or 'default'

        selected_profile = next((p for p in profiles if p.get('name') == profile_name), None)
        if not selected_profile and profile_name != 'default':
            selected_profile = next((p for p in profiles if p.get('name') == 'default'), None)
        if not selected_profile:
            return (None, None)

        access_key_id = (selected_profile.get('access_key_id') or
                         selected_profile.get('AccessKeyId') or
                         selected_profile.get('accessKeyId'))
        access_key_secret = (selected_profile.get('access_key_secret') or
                             selected_profile.get('AccessKeySecret') or
                             selected_profile.get('accessKeySecret'))

        return (access_key_id, access_key_secret)

    def authenticate(self, access_key_id=None, access_key_secret=None, profile=None, **kwargs):

        try:
            if not (access_key_id and access_key_secret):
                profile_access_key_id, profile_access_key_secret = self._get_profile_credentials(profile=profile)
                access_key_id = access_key_id or profile_access_key_id
                access_key_secret = access_key_secret or profile_access_key_secret

            access_key_id = access_key_id if access_key_id else input('Access Key ID:')
            access_key_secret = access_key_secret if access_key_secret else getpass('Secret Access Key:')

            credentials = AccessKeyCredential(access_key_id=access_key_id, access_key_secret=access_key_secret)

            # get caller details
            client = AcsClient(credential=credentials)
            response = client.do_action_with_exception(
                GetCallerIdentityRequest.GetCallerIdentityRequest())
            response_decoded = json.loads(response)

            return AliyunCredentials(credentials, response_decoded)

        except Exception as e:
            raise AuthenticationException(e)
