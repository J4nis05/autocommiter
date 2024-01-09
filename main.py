import git

with open('api.key', 'r') as file:
    token = file.read()

repo = git.Repo('./')
commit_message = 'Commit Test from Script'
repo.git.add('--all')
repo.index.commit(commit_message)

# Push changes to GitHub
origin = repo.remote(name='origin')
origin_url = origin.url.replace('https://', f'https://{token}@')
origin.url = origin_url
origin.push()
print("Changes pushed to GitHub.")
