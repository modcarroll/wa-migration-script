# Watson Assistant Migration Tool

This is a script to migrate skills from 3 instances of Watson Assistant to 1 instance of Watson Assistant.

## Directions

1. Open `WA_Transfer.py` and update the credentials block with your Watson Assistant credentials. The variable `wa_source_credentials` is an array containing a set of 3 Watson Assistant instance credentials. These are the instances that you want to migrate FROM. `wa_target_credentials` is the variable that will hold the Watson Assistant instance credentials that you wish to migrate TO.

2. Once you have updated the credentials, run the script: `python3 WA_Transfer.py`

### Note

This script will NOT migrate logs as Watson Assistant does not currently support importing logs.
