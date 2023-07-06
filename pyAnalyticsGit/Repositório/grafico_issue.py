from collections import defaultdict
import matplotlib.pyplot as plt
import os
from connect import Connect

class GraficoIssue:
    def __init__(self):
        connect = Connect()
        self.issues = connect.connect_issue()

    def criar_grafico_issue(self):
        issue_authors = defaultdict(int)
        for issue in self.issues:
            author = issue["user"]["login"]
            issue_authors[author] += 1

        authors = list(issue_authors.keys())
        issue_numbers = list(issue_authors.values())

        plt.bar(authors, issue_numbers, color='steelblue')
        plt.xlabel('Autores')
        plt.ylabel('Número de Issues', color='steelblue')
        plt.title('Gráfico de Issues por Autor', fontsize=16, color='black')
        plt.xticks(rotation=45)
        plt.gca().set_facecolor('black')
        if os.path.exists('pyAnalyticsGit/grafico_issues.png'):
            os.remove('pyAnalyticsGit/grafico_issues.png')

        plt.savefig('pyAnalyticsGit/grafico_issues.png')
        plt.close()