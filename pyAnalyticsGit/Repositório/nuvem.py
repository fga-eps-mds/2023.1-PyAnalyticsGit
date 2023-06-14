from wordcloud import STOPWORDS, WordCloud
from commit import Commits
from connect import Connect
import os
import matplotlib.pyplot as plt

class AnaliseTextual:
    def __init__(self):
        connect = Connect()
        self.commits = connect.connect_commit()
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
        plt.show()

analise = AnaliseTextual()
analise.gerar_nuvem_commits()