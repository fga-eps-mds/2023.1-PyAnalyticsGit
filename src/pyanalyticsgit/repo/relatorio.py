import os
from .commit import Commits
from .connect import api_name, api_user
from .issue import Issue
from .milestone import Milestone

# diretorio_raiz = os.path.abspath(os.path.dirname(__file__))
diretorio_raiz = os.getcwd()

nome_pasta = "docs"

caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)

class Relatorio:
    """Classe para gerar relatório de commits, issues e milestones"""
    def __init__(self):
        """Construtor da classe Relatorio"""
        self.nome_arquivo = "relatorio_padrao.md"
        self.titulo = "# Relatório dos dados do Repositório"
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
        self.caminho_arquivo = os.path.join(caminho_pasta, self.nome_arquivo)
        with open(self.caminho_arquivo, 'w+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n\n')

    def gerar_relatorio(self,user = api_user, repo = api_name):
        """Método que gera o relatório de commits, issues e milestones do repositório e salva em um arquivo .md"""
        if os.path.exists(self.caminho_arquivo):
            os.remove(self.caminho_arquivo)
            
        with open(self.caminho_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n') 

        grafico_tabela_commit = Commits(user,repo)
        grafico_tabela_commit.criar_grafico_commit()

        with open(self.caminho_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Commits\n\n")
            arq.write("\n## Grafico de Commits\n\n")
            arq.write("<div align='center'>\n\n")
            arq.write(f'![Grafico de Commits](grafico.png)\n\n')
            arq.write("</div>\n\n")

        grafico_tabela_commit.criar_tabela_commit(self.caminho_arquivo)

        grafico_tabela_commit.gerar_nuvem_commits()

        with open(self.caminho_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("\n## Nuvem de Palavras dos Commits\n\n")
            arq.write("<div align='center'>\n\n")
            arq.write("![Nuvem de Palavras dos Commits](grafico_nuvem.png)\n\n")
            arq.write("</div>\n\n")

        grafico_tabela_issue = Issue(user,repo)
        grafico_tabela_issue.criar_grafico_issue()

        with open(self.caminho_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Issues\n\n")
            arq.write("## Gráfico de Issues\n\n")
            arq.write("<div align='center'>\n\n")
            arq.write("![Gráfico de Issues](grafico_issue.png)\n\n")
            arq.write("</div>\n\n")

        grafico_tabela_issue.criar_tabela_issue(self.caminho_arquivo)
        
        grafico_tabela_issue.criar_grafico_pizza()

        with open(self.caminho_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("## Gráfico de Pizza das Tags de Issues\n\n")
            arq.write("<div align='center'>\n\n")
            arq.write("![Gráfico de Pizza de Issues](grafico_pizza.png)\n\n")
            arq.write("</div>\n\n")

        grafico_tabela_milestone = Milestone(user, repo)
        grafico_tabela_milestone.criar_grafico_milestones()

        with open(self.caminho_arquivo, 'a+', encoding="utf-8") as arq:
            arq.write("# Milestones\n\n")
            arq.write("## Gráfico de Milestones\n\n")
            arq.write("<div align='center'>\n\n")
            arq.write("![Gráfico de Milestones](grafico_milestone.png)\n\n")
            arq.write("</div>\n\n")

        grafico_tabela_milestone.criar_tabela_milestone(self.caminho_arquivo)
    