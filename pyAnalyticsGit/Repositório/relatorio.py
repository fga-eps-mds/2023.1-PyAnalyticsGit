from grafico import Grafico
from nuvem import AnaliseTextual
from commit import Commits

class relatorio:
    def __init__(self):
        self.nome_arquivo = "relatorio_padrao.md"
        self.titulo = "## PyAnalyticsGit - Relatório automatizado"
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n')

    def gerar_relatorio(self, username, reponame):
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n')

        commits = Commits()
        commits.connect(username, reponame)

        with open(self.nome_arquivo, 'a+') as arq:
            arq.write('\n### Grafico de Barras\n\n')
            arq.write('![Grafico de Barras](grafico.png)\n\n')
            arq.write('### Nuvem de Palavras\n\n')
            arq.write('![Nuvem de Palavras](nuvem_palavras.png)\n\n')

template = relatorio()
template.gerar_relatorio("fga-eps-mds","2023.1-PyAnalyticsGit")            

template = relatorio()
