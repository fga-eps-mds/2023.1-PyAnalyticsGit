import matplotlib.pyplot as plt
import os
import numpy as np
from .connect import Connect,api_user,api_name

# diretorio_raiz = os.path.abspath(os.path.dirname(__file__))
diretorio_raiz = os.getcwd()

nome_pasta = "docs"
grafico_milestone = 'grafico_milestone.png'
grafico_miles_tag = 'grafico_miles_tag.png'

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

        plt.figure(figsize=(8, 9))
        plt.bar(milestones, issue_counts, color='darkgreen')
        plt.xlabel('Milestone')
        plt.ylabel('Número de Issues', color='darkgreen')
        plt.title('Gráfico de Milestones', fontsize=16, color='black')
        plt.gca().set_facecolor('black')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if os.path.exists(os.path.join(caminho_pasta,grafico_milestone)):
            os.remove(os.path.join(caminho_pasta,grafico_milestone))  
             
        plt.savefig(os.path.join(caminho_pasta,grafico_milestone))
        plt.close()

    def criar_grafico_miles_tag(self):
        """Método que cria o gráfico de tags por milestones"""
        milestone_labels = [milestone.get('title') for milestone in self.milestones]
        milestone_tags = [[] for _ in self.milestones]

        for i, milestone in enumerate(self.milestones):
            seen_tags = set()
            for issue in self.issues:
                if 'milestone' in issue and issue['milestone'] is not None and issue['milestone'].get('title') == milestone.get('title'):
                    issue_labels = issue.get('labels', [])
                    for label in issue_labels:
                        tag = label.get('name')
                        if tag not in seen_tags:
                            milestone_tags[i].append(tag)
                            seen_tags.add(tag)

        fig, ax = plt.subplots(figsize=(10, len(self.milestones) * 0.5))
        colors = plt.cm.tab20(np.linspace(0, 1, len(milestone_tags)))

        max_tag_width = max(len(tag) for tags in milestone_tags for tag in tags)  

        for i, tags in enumerate(milestone_tags):
            for j, tag in enumerate(tags):
                ax.scatter(j + 1, i, color=colors[i], s=400, marker='s')  
                ax.text(j + 1, i, tag, ha='center', va='center', color='white')

        ax.set_ylim(-0.5, len(self.milestones) - 0.5)  
        ax.set_xlim(0.5, max(map(len, milestone_tags)) + 0.5)  
        ax.set_yticks(range(len(self.milestones)))
        ax.set_yticklabels(milestone_labels, ha='right', fontsize=10, fontweight='bold')  
        ax.set_xticks([])  
        ax.set_xlabel('Tags', fontsize=12, fontweight='bold')  
        ax.set_title('Tags por Milestone', fontsize=16, fontweight='bold') 
        bar_height = 0.8  
        ax.set_ylim(-bar_height, len(self.milestones) - 1 + bar_height)
        ax.set_facecolor('black')  
        plt.tight_layout()
        if os.path.exists(os.path.join(caminho_pasta,grafico_miles_tag)):
            os.remove(os.path.join(caminho_pasta,grafico_miles_tag))  
             
        plt.savefig(os.path.join(caminho_pasta,grafico_miles_tag))
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