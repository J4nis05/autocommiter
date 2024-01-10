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

### Alternative Way
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    git config --global credential.helper store
    git credential-cache exit

    git credential-store --file ~/.git-credentials store
    echo "https://<USERNAME>:<YOUR_TOKEN>@github.com" >> ~/.git-credentials

## Dependencies
    Generate:
    pip freeze > requirements.txt
    Install:
    pip install -r requirements.txt

## Setting up Crontab
    crontab -e
    0 15 * * * /usr/bin/python3 /path/to/main.py
    (Commit happens at 15.00 Hours everyday)
