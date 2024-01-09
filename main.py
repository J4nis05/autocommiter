import git

# Commit Changes
repo = git.Repo('./')
commit_message = 'Commit Test using the Credential Manager'
repo.git.add('--all')
repo.index.commit(commit_message)

# Push changes to GitHub
origin = repo.remote(name='origin')
origin.push()
print("Changes pushed to GitHub.")
