import requests
from datetime import datetime

class Milestone:

    def __init__(self):
        pass


    def get_milestones(self,userName,repoName):
        self.userName = userName
        self.repoName = repoName
        # https://api.github.com/repos/fga-eps-mds/2023.1-PyAnalyticsGit/milestones
        url =f'https://api.github.com/repos/{userName}/{repoName}/milestones'
        response = requests.get(url)

        if response.status_code == 200:
            self.milestones = response.json()
        else:
            print(f'Falha ao obter os detalhes do repositório {repoName}.')
            exit()

    def list_milestone(self):
        arq = open(f'Milestone.md','w+')
        for milestone in self.milestones:
            data_inicio = milestone["created_at"]
            data_formatada = datetime.strptime(data_inicio, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
            arq.write(f'- Título: {milestone["title"]}\n')
            arq.write(f'- Cirado em: {data_formatada}\n')
            arq.write(f'- Descrição: {milestone["description"]}\n')
            arq.write(f'- Issues Abertas: {milestone["open_issues"]}\n')
            arq.write(f'- Issues Fechadas: {milestone["closed_issues"]}\n')
            arq.write('---------------------\n')


milestone = Milestone()
milestone.get_milestones("fga-eps-mds","2023.1-PyAnalyticsGit")
milestone.list_milestone()
