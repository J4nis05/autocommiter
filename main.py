import git

with open('api.key', 'r') as file:
    token = file.read()

repo = git.Repo('./')

print(repo.git.status())
print(token)
