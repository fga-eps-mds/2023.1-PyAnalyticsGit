import os
from grafico import Grafico
from grafico_issue import GraficoIssue
from grafico_pizza import GraficoPizza
from nuvem import AnaliseTextual
from tabela_issue import TabelaIssue
from tabela import Tabela
#from commit import Commits
#from issue import Issue
#from milestone import Milestone #Import Milestone

class Relatorio:
    def __init__(self):
        self.nome_arquivo = "relatorio_padrao.md"
        self.titulo = "## - Relatório automatizado"

        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n\n')

    def gerar_relatorio(self):
        if os.path.exists(self.nome_arquivo):
            os.remove(self.nome_arquivo)
            
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n') 

        grafico = Grafico()
        grafico.criar_grafico()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Commits\n\n")
            arq.write("\n## Grafico de Commits\n\n")
            arq.write("![Grafico de Commits](pyAnalyticsGit/grafico.png)\n\n")

        tabela_commit = Tabela()
        tabela_commit.criar_tabela(self.nome_arquivo)

        nuvem_palavras = AnaliseTextual()
        nuvem_palavras.gerar_nuvem_commits()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("\n## Nuvem de Palavras dos Commits\n\n")
            arq.write("![Nuvem de Palavras dos Commits](pyAnalyticsGit/nuvem.png)\n\n")

        grafico_issue = GraficoIssue()
        grafico_issue.criar_grafico_issue()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Issues\n\n")
            arq.write("## Gráfico de Issues\n\n")
            arq.write("![Gráfico de Issues](pyAnalyticsGit/grafico_issues.png)\n\n")

        tabela_issue = TabelaIssue()
        tabela_issue.criar_tabela_issue(self.nome_arquivo)
        
        grafico_pizza = GraficoPizza()
        grafico_pizza.criar_grafico_pizza()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("## Gráfico de Pizza das Tags de Issues\n\n")
            arq.write("![Gráfico de Pizza de Issues](pyAnalyticsGit/grafico_pizza.png)\n\n")

relatorio = Relatorio()
relatorio.gerar_relatorio()  

   #def exec_issues(self):
            #obj_issue = Issue()
            #obj_issue.listar_issue()

    #def exec_milestones(self):
            #obj_milestone = Milestone()
            #obj_milestone.list_milestone()

    #def exec_commits(self):
            #obj_commits = Commits()
            #obj_commits.listar_commits()