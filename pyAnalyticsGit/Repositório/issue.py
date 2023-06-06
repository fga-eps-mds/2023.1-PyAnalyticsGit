import requests

class Issue:
    def __init__(self):
        pass

    def connect(self,username,reponame):
        self.username = username
        self.reponame = reponame

        page = 1
        per_page = 30
        self.all_issues = []

        while True:           
            response = requests.get(f'https://api.github.com/repos/{username}/{reponame}/issues?state=all&page={page}&per_page={per_page}')

            if response.status_code == 200:
                self.issues = response.json()
                self.all_issues.extend(self.issues)
                #print("conexão estabelecida\n")

                if len(self.issues) < per_page:
                    break
                else:
                    page += 1

            else:
                print(f'Falha ao obter os detalhes do repositório {reponame}.')
                print(f'StatusCode: {response.status_code}')
                break

    def listar_issue(self):
        arq = open("relatorio_padrao.md","a+")
        arq.write('# Issues\n')
        for issue in self.all_issues:
            arq.seek(0)
            if str(issue["number"]) not in arq.read():
                arq.write(f'- Título: {issue["title"]}\n')
                arq.write(f'- Estado: {issue["state"]}\n')
                arq.write(f'- Número: {issue["number"]}\n')
                labels = []
                for label in issue["labels"]:
                    labels.append(label["name"])
                #arq.write("Labels:",", ".join(labels))
                arq.write(f'- Labels: {", ".join(labels)}\n')
                arq.write('---------------------\n')

    def listar_issue_label(self,label):
        arq = open(f'issues_{label}.md',"w+")
        arq.write(f'### Todas as issues de **{label}:**\n\n')
        c = 0
        for issue in self.all_issues:
            for labels in issue["labels"]:
                if labels["name"] == label:
                    arq.write(f'- Título: {issue["title"]}\n')
                    arq.write(f'- Estado: {issue["state"]}\n')
                    arq.write(f'- Número: {issue["number"]}\n')
                    arq.write('---------------------\n')
                    c = c + 1
        if c == 0 :
            print("Label não encontrada")
        else:
            print(c)              
                    


#issue1 = Issue()
#issue2 = Issue()

#issue1.connect("Tiago1604","teste-github-vscode")
#issue1.listar_issue()

#issue2.connect("fga-eps-mds","2023.1-PyAnalyticsGit")
#issue2.listar_issue_label("documentation")
#issue2.listar_issue()