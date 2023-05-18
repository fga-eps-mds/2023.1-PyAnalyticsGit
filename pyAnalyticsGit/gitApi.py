import requests
#Get user information


user = f'https://api.github.com/users/mateus9levy'

#Informacoes sobre o repositorio https://api.github.com/repos/{Owner}/{repository Name}

repo = f'https://api.github.com/repos/fga-eps-mds/2023.1-PyAnalyticsGit'
# commits dentro de um repositorio
commits = f'https://api.github.com/repos/fga-eps-mds/2023.1-PyAnalyticsGit/commits'

# informacoes sobre issues
issues = f'https://api.github.com/repos/fga-eps-mds/2023.1-PyAnalyticsGit/issues/events'
response = requests.get(commits)

data = response.json()

print(data)