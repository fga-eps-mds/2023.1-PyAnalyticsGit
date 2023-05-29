import requests

class Issue:
    def __init__(self):
        pass

    def connect(self,username,reponame):
        self.username = username
        self.reponame = reponame

        url = f'https://api.github.com/repos/{username}/{reponame}/issues?state=all'

        response = requests.get(url)

        if response.status_code == 200:
            self.issues = response.json()
            print("conexão estabelecida\n")
        else:
            print(f'Falha ao obter os detalhes do repositório {reponame}.')
            exit()

    def listar_issue(self):
        for issue in self.issues:
            print(f'Título: {issue["title"]}')
            print(f'Estado: {issue["state"]}')
            print(f'Número: {issue["number"]}')
            labels = []
            for label in issue["labels"]:
                labels.append(label["name"])
            print("Labels:",", ".join(labels))
            print('---------------------')

    def listar_issue_label(self,label):
        c = 0
        for issue in self.issues:
            for labels in issue["labels"]:
                if labels["name"] == label:
                    print(f'Título: {issue["title"]}')
                    print(f'Estado: {issue["state"]}')
                    print(f'Número: {issue["number"]}')
                    print('---------------------')
                    c = c + 1
        if c == 0 :
            print("Label não encontrada")              
                    


#issue1 = Issue()
issue2 = Issue()

#issue1.connect("Tiago1604","teste-github-vscode")
#issue1.listar_issue()

issue2.connect("fga-eps-mds","2023.1-PyAnalyticsGit")
issue2.listar_issue()