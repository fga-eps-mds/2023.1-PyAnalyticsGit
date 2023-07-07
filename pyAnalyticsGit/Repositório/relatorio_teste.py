import os
from graficos import Graficos
from tabelas import Tabelas
#from commit import Commits
#from issue import Issue
#from milestone import Milestone #Import Milestone

class Relatorio:
    def __init__(self):
        self.nome_arquivo = "relatorio_padrao_teste.md"
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

        grafico = Graficos()
        grafico.criar_grafico()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Commits\n\n")
            arq.write("\n## Grafico de Commits\n\n")
            arq.write("![Grafico de Commits](pyAnalyticsGit/grafico.png)\n\n")

        tabela = Tabelas()
        tabela.criar_tabela(self.nome_arquivo)

        grafico.gerar_nuvem_commits()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("\n## Nuvem de Palavras dos Commits\n\n")
            arq.write("![Nuvem de Palavras dos Commits](pyAnalyticsGit/nuvem.png)\n\n")

        grafico.criar_grafico_issue()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Issues\n\n")
            arq.write("## Gráfico de Issues\n\n")
            arq.write("![Gráfico de Issues](pyAnalyticsGit/grafico_issues.png)\n\n")

        tabela.criar_tabela_issue(self.nome_arquivo)
        
        grafico.criar_grafico_pizza()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("## Gráfico de Pizza das Tags de Issues\n\n")
            arq.write("![Gráfico de Pizza de Issues](pyAnalyticsGit/grafico_pizza.png)\n\n")

        grafico.criar_grafico_milestones()

        with open(self.nome_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Milestones\n\n")
            arq.write("## Gráfico de Milestones\n\n")
            arq.write("![Gráfico de Milestones](pyAnalyticsGit/grafico_milestone.png)\n\n")

        tabela.criar_tabela_milestone(self.nome_arquivo)         

relatorio = Relatorio()
relatorio.gerar_relatorio()  