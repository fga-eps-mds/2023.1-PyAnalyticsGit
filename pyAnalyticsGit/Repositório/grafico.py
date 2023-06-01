from collections import defaultdict
import matplotlib.pyplot as plt
from commit import Commits


class Grafico:
    def __init__(self, commits):
        self.commits = commits

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
        plt.savefig('pyAnalyticsGit/grafico.png')

commits_obj = Commits()
commits_obj.connect("fga-eps-mds","2023.1-PyAnalyticsGit")

grafico_obj = Grafico(commits_obj.commits)
grafico_obj.criar_grafico()