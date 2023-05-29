import requests

class Commits:
    def __init__(self):
        pass

    def connect(self,username,reponame):
        self.username = username
        self.reponame = reponame

        url = f'https://api.github.com/repos/{username}/{reponame}/commits'

        response = requests.get(url)

        if response.status_code == 200:
            self.commits = response.json()
            print("conexão estabelecida\n")
        else:
            print(f'Falha ao obter os detalhes do repositório {reponame}.')
            exit()

    def listar_commits(self):
        arq = open(f'relatorio_commits.md','w+')
        for commit in self.commits:
            arq.write(f'- hash do commit: {commit["sha"]}\n')
            arq.write(f'- author do commit: {commit["commit"]["author"]["name"]}\n')
            arq.write(f'- Mensagem: {commit["commit"]["message"]}\n')
            arq.write("----------------------------\n")

    def listar_commits_author(self,author):
        arq = open(f'relatório_{author}.md','w+')
        arq.write(f'#Título dos commits de {author}:\n')
        arq.write('\n')
        for commit in self.commits:
            if author == commit["commit"]["author"]["name"]:
                arq.write(f'- {commit["commit"]["message"]}\n')
            else:
                print("Essa pessoa não realizou commits")
                exit()

c1 = Commits()
c1.connect("Tiago1604","teste-github-vscode")
c1.listar_commits()
c1.listar_commits_author('Tiago1604')