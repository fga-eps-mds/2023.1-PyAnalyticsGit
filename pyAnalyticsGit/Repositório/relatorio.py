from grafico import Grafico
from nuvem import AnaliseTextual
from commit import Commits
from issue import Issue

class Relatorio:
    def __init__(self):
        self.nome_arquivo = "relatorio_padrao.md"
        self.titulo = "## PyAnalyticsGit - Relatório automatizado"
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n\n')

    def gerar_relatorio(self, username, reponame):
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n') 

        commits = Commits()
        commits.connect(username, reponame)

        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if ("### Grafico de Barras" or "### Nuvem de Palavras") not in arq.read():
                arq.write('\n### Grafico de Barras\n\n')
                arq.write('![Grafico de Barras](pyAnalyticsGit/grafico.png)\n\n')
                arq.write('### Nuvem de Palavras\n\n')
                arq.write('![Nuvem de Palavras](pyAnalyticsGit/nuvem.png)\n\n')

    def exec_issues(self):
            obj_issue = Issue()
            obj_issue.connect("fga-eps-mds","2023.1-PyAnalyticsGit")
            obj_issue.listar_issue()
                

obj_relatorio = Relatorio()
obj_relatorio.exec_issues()


template = Relatorio()
template.gerar_relatorio("fga-eps-mds","2023.1-PyAnalyticsGit")            

template = Relatorio()
