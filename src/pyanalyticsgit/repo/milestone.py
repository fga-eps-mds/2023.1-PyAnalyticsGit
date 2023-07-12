from collections import defaultdict
import matplotlib.pyplot as plt
import os
from datetime import datetime
from .connect import Connect,api_user,api_name

# diretorio_raiz = os.path.abspath(os.path.dirname(__file__))
diretorio_raiz = os.getcwd()

nome_pasta = "docs"
grafico_milestone = 'grafico_milestone.png'

caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)

class Milestone:
    """Classe para gerar relatório de milestones"""
    def __init__(self, user = api_user, repo = api_name):
        """Construtor da classe Milestone"""
        connect = Connect()
        self.milestones = connect.connect_milestone(user,repo)
        self.issues = connect.connect_issue(user,repo)
        self.nome_arquivo = 'relatorio_padrao.md'
        self.caminho_arquivo = os.path.join(caminho_pasta,self.nome_arquivo)

    def criar_grafico_milestones(self):
        """Método que cria o gráfico de milestones"""
        milestone_issues = {}
        for milestone in self.milestones:
            milestone_title = milestone["title"]
            milestone_issues[milestone_title] = 0

        for issue in self.issues:
            issue_milestone = issue["milestone"]
            if issue_milestone:
                milestone_title = issue_milestone["title"]
                if milestone_title in milestone_issues:
                    milestone_issues[milestone_title] += 1

        milestones = list(milestone_issues.keys())
        issue_counts = list(milestone_issues.values())

        plt.bar(milestones, issue_counts, color='darkgreen')
        plt.xlabel('Milestone')
        plt.ylabel('Número de Issues', color='darkgreen')
        plt.title('Gráfico de Milestones', fontsize=16, color='black')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if os.path.exists(os.path.join(caminho_pasta,grafico_milestone)):
            os.remove(os.path.join(caminho_pasta,grafico_milestone))  
             
        plt.savefig(os.path.join(caminho_pasta,grafico_milestone))
        plt.close()

    def criar_tabela_milestone(self, relatorio_file):
        """Método que cria a tabela de milestones e issues"""
        milestone_issues = {}
        sprint_issues = {}

        for milestone in self.milestones:
            milestone_title = milestone["title"]
            milestone_issues[milestone_title] = 0
            sprint_issues[milestone_title] = []

        for issue in self.issues:
            issue_milestone = issue["milestone"]
            if issue_milestone:
                milestone_title = issue_milestone["title"]
                if milestone_title in milestone_issues:
                    milestone_issues[milestone_title] += 1
                    sprint_issues[milestone_title].append(issue["title"])

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Milestones e Issues\n\n")
            file.write("| Milestone | Número de Issues | Lista de Issues |\n")
            file.write("| --- | ---: | --- |\n")

            for milestone_title, issue_count in milestone_issues.items():
                issues_list = ", ".join(sprint_issues[milestone_title])
                file.write(f"| {milestone_title} | {issue_count} | {issues_list} |\n")

            file.write("\n")