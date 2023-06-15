from collections import defaultdict
import matplotlib.pyplot as plt
import os
from connect import Connect
from commit import Commits


class Grafico:
    def __init__(self):
        connect = Connect()
        self.commits = connect.connect_commit()

    def criar_grafico(self):
        commit_authors = defaultdict(int)
        for commit in self.commits:
            author = commit["commit"]["author"]["name"]
            commit_authors[author] += 1

        authors = list(commit_authors.keys())
        commit_numbers = list(commit_authors.values())

        plt.bar(authors, commit_numbers, color='darkred')
        plt.xlabel('Autores')
        plt.ylabel('Número de Commits', color='darkred')
        plt.title('Gráfico de Commits por Autor', fontsize=16, color='black')
        plt.xticks(rotation=45)
        plt.gca().set_facecolor('black')
        if os.path.exists('pyAnalyticsGit/grafico.png'):
            os.remove('pyAnalyticsGit/grafico.png')

        plt.savefig('pyAnalyticsGit/grafico.png')
        plt.show()

grafico_obj = Grafico()
grafico_obj.criar_grafico()