![PyPI pyversions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

# Watson Assistant Migration Tool

This is a script to migrate skills from 3 instances (assuming dev, test, prod) of Watson Assistant to 1 instance of Watson Assistant.

## Directions

1. Open `WA_Transfer.py` and update the credentials block with your Watson Assistant credentials. The variable `wa_source_credentials` is an array containing a set of 3 Watson Assistant instance credentials. These are the instances that you want to migrate FROM. `wa_target_credentials` is the variable that will hold the Watson Assistant instance credentials that you wish to migrate TO.

2. Once you have updated the credentials, run the script: `python3 WA_Transfer.py` or `python WA_Transfer.py`

## delete.py

**DANGER** This script WILL delete every skill in your instance of Watson Assistant. ONLY use once you have confirmed that your skills have been properly backed up/migrated.

## Note

This script will NOT migrate logs as Watson Assistant does not currently support importing logs.
