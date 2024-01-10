# autocommiter
A Tool that commits automatically
using Python and crontab

## Add Access Token To Credential Store
### With UI
    git credential-manager github login
    --> Add the Token in the "Token" Tab

### Without UI
    git credential-manager github login --no-ui
    --> Enter "3" To Add a Token
    --> Paste the Token

## Dependencies
    Generate:
    pip freeze > requirements.txt
    Install:
    pip install -r requirements.txt

## Setting up Crontab
    crontab -e
    0 15 * * * /usr/bin/python3 /path/to/main.py
    (Commit happens at 15.00 Hours everyday)
