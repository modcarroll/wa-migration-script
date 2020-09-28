###########################################################
# Author: Morgan Langlais, IBM
# Contact: morgandlanglais@gmail.com
# This script will delete ALL skills in
# the indicated Watson Assistant instance
###########################################################

import json
import ibm_watson
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

wa_target_credentials = {'wa_version':'2020-04-01', 'wa_apikey':'123apikey', 'wa_url':'https://api.us-south.assistant.watson.cloud.ibm.com/instances/123myinstanceid'}

authenticator_target = IAMAuthenticator(wa_target_credentials['wa_apikey'])

assistant_service = ibm_watson.AssistantV1(
    version = wa_target_credentials['wa_version'],
    authenticator = authenticator_target
)
assistant_service.set_service_url(wa_target_credentials['wa_url']);

list_wrkspc_response = assistant_service.list_workspaces().get_result()['workspaces']

for space in list_wrkspc_response:
  response=assistant_service.delete_workspace(
      workspace_id=space['workspace_id']
  ).get_result()

  print(json.dumps(response, indent=2))
