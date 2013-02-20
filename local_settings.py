'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACf4d73f87dd7d10f53cf2b86d65d24b6a" 
AUTH_TOKEN = "d74718b19db3633c5a7548ba65fa03ed"
BSSSPAM_APP_SID = "AP728b57234a312d7637585381e86c6d62"
BSS_SPAM_ID = "+18563430082"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
