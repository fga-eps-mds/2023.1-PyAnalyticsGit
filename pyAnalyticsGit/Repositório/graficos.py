from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
import os
from connect import Connect

class Graficos:
    def __init__(self):
        connect = Connect()
        self.commits = connect.connect_commit()
        self.issues = connect.connect_issue()
        self.milestones = connect.connect_milestone()
        self.palavras_ignoradas = ["o","a","e","i","u","de","des","da","das","do","dos","md","para","que"]

    def listar_nomes_commits(self):
        nomes_commits = []
        for commit in self.commits:
            nome_commit = commit["commit"]["message"]
            nomes_commits.append(nome_commit)
        return nomes_commits    

    def gerar_nuvem_commits(self):
        nomes_commits = self.listar_nomes_commits()
        texto = " ".join(nomes_commits)

        stopwords = set(STOPWORDS)
        stopwords.update(self.palavras_ignoradas) 

        wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords,
                              colormap='viridis', max_words=300).generate(texto)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear') 
        plt.axis('off')
        plt.title('Nuvem de palavras com nomes dos Commits')

        if os.path.exists('pyAnalyticsGit/nuvem.png'):
            os.remove('pyAnalyticsGit/nuvem.png')

        plt.savefig('pyAnalyticsGit/nuvem.png')
        plt.close()    

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
        plt.close()

    def criar_grafico_pizza(self):
        label_count = defaultdict(int)
        total_issues = len(self.issues)

        for issue in self.issues:
            labels = issue["labels"]
            for label in labels:
                label_count[label["name"]] += 1

        labels = list(label_count.keys())
        counts = list(label_count.values())
        percentages = [(count / total_issues) * 100 for count in counts]
        sorted_labels, sorted_percentages = zip(*sorted(zip(labels, percentages), key=lambda x: x[1], reverse=True))

        fig, ax = plt.subplots() 
        ax.pie(sorted_percentages, labels=sorted_labels, shadow=True, autopct='%1.1f%%', startangle=90)
        ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.5), fontsize='medium', title='Tags')
        ax.set_title('Grafico de Issues por Tags')
        ax.axis('equal')
        if os.path.exists('pyAnalyticsGit/grafico_pizza.png'):
            os.remove('pyAnalyticsGit/grafico_pizza.png')   

        plt.savefig('pyAnalyticsGit/grafico_pizza.png')
        plt.close()

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

    def criar_grafico_milestones(self):
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
        if os.path.exists('pyAnalyticsGit/grafico_milestone.png'):
            os.remove('pyAnalyticsGit/grafico_milestone.png')  
             
        plt.savefig('pyAnalyticsGit/grafico_milestone.png')
        plt.close()