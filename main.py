import git

repo = git.Repo('./')

print(repo.git.status())
