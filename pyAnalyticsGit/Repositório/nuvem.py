from wordcloud import STOPWORDS, WordCloud
from commit import Commits
import matplotlib.pyplot as plt

class AnaliseTextual:
    def __init__(self):
        self.commits = None
        self.palavras_ignoradas = ["o","a","e","i","u","de","des","da","das","do","dos","md","para","que"]

    def conectar_repositorio(self,username,reponame):   
        commits = Commits()
        commits.connect("fga-eps-mds","2023.1-PyAnalyticsGit")
        self.commits = commits.commits

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
        plt.show()


analise = AnaliseTextual()
analise.conectar_repositorio("fga-eps-mds","2023.1-PyAnalyticsGit")
analise.gerar_nuvem_commits()