###########################################################
# Author: Morgan Langlais, IBM
# Contact: morgandlanglais@gmail.com
# Link: https://github.com/modlanglais/wa-migration-script
###########################################################

import json
import ibm_watson
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

############################
# Do not delete this block
wa_credentials = ''
############################

####### Watson Assistant creds #######
wa_source_credentials = [{'wa_version':'2020-04-01', 'wa_apikey':'123apikey', 'wa_url':'https://gateway.watsonplatform.net/assistant/api'},{'wa_version':'2020-04-01', 'wa_apikey':'123apikey', 'wa_url':'https://gateway.watsonplatform.net/assistant/api'},{'wa_version':'2020-04-01', 'wa_apikey':'123apikey', 'wa_url':'https://api.us-south.assistant.watson.cloud.ibm.com/instances/123myinstanceid'}]

wa_target_credentials = {'wa_version':'2020-04-01', 'wa_apikey':'123apikey', 'wa_url':'https://api.us-south.assistant.watson.cloud.ibm.com/instances/123myinstanceid'}
#################################################

############################################
# Watson Assistant transfer
############################################
authenticator_target = IAMAuthenticator(wa_target_credentials['wa_apikey'])

assistant_target = ibm_watson.AssistantV1(
    version = wa_target_credentials['wa_version'],
    authenticator = authenticator_target
)
assistant_target.set_service_url(wa_target_credentials['wa_url']);

print("Starting Watson Assistant transfer...")
print("")

if wa_source_credentials != '':
    for creds in wa_source_credentials:
        wa_version = creds['wa_version']
        wa_apikey = creds['wa_apikey']
        wa_url = creds['wa_url']

        if(wa_version == '' or wa_apikey == '' or wa_url == ''):
            print("No or invalid Watson Assistant credentials detected. Skipping.")
        else:
            authenticator = IAMAuthenticator(wa_apikey)

            assistant_service=ibm_watson.AssistantV1(
                version = wa_version,
                authenticator = authenticator
            )
            assistant_service.set_service_url(wa_url);

            try:
                list_wrkspc_response = assistant_service.list_workspaces().get_result()['workspaces']
            except ApiException as ex:
                print("Method failed with status code " + str(ex.code) + ": " + ex.message)

            print()
            for space in list_wrkspc_response:
                print()
                print("--> Migrating "+ space['name'] + " <--")

                workspace_response = []
                log_response = []

                try:
                    workspace_response = assistant_service.get_workspace(
                        workspace_id = space['workspace_id'],
                        export=True
                    ).get_result()

                    response = assistant_target.create_workspace(
                        name=workspace_response['name'],
                        description=workspace_response['description']
                    ).get_result()

                    print("")
                    print(response)
                    print("")

                    print(space['name'] + " migrated ✅")
                    print("")
                except (ApiException, Exception) as ex:
                    print(space['name'] + " migration failed. " + str(ex.code) + ": " + ex.message)

    print("")
    print("Migration complete.")
