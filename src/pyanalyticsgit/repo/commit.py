from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
import os
from .connect import  Connect, api_name, api_user

# diretorio_raiz = os.path.abspath(os.path.dirname(__file__))
diretorio_raiz = os.getcwd()

nome_pasta = "docs"
grafico = 'grafico.png'
grafico_nuvem = 'grafico_nuvem.png'

caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)


class Commits:
    """Classe para gerar gráficos e tabelas de commits"""
    def __init__(self, user = api_user, repo=api_name):
        """Construtor da classe Commits"""
        connect = Connect()
        self.commits = connect.connect_commit(user,repo)
        self.palavras_ignoradas = ["o","a","e","i","u","de","des","da","das","do","dos","md","para","que"]

    def listar_nomes_commits(self):
        """Método que retorna uma lista com os nomes dos commits"""
        nomes_commits = []
        for commit in self.commits:
            nome_commit = commit["commit"]["message"]
            nomes_commits.append(nome_commit)
        return nomes_commits    

    def gerar_nuvem_commits(self):
        """Método que gera uma nuvem de palavras com os nomes dos commits"""
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

        if os.path.exists(os.path.join(caminho_pasta,grafico_nuvem)):
            os.remove(os.path.join(caminho_pasta,grafico_nuvem))

        plt.savefig(os.path.join(caminho_pasta,grafico_nuvem))
        plt.close()    

    def criar_grafico_commit(self):
        """Método que cria um gráfico de barras com os nomes dos autores e a quantidade de commits"""
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
        if os.path.exists(os.path.join(caminho_pasta,grafico)):
            os.remove(os.path.join(caminho_pasta,grafico))

        plt.savefig(os.path.join(caminho_pasta,grafico))
        plt.close()

    def criar_tabela_commit(self, relatorio_file):
        """Método que cria uma tabela com os nomes dos autores e a quantidade de commits por autor"""
        commit_count = {}
        commit_datas = {}
        for commit in self.commits:
            author = commit["commit"]["author"]["name"]
            if author in commit_count:
                commit_count[author] += 1
                commit_datas[author].append(commit["commit"]["author"]["date"])
            else:
                commit_count[author] = 1
                commit_datas[author] = [commit["commit"]["author"]["date"]]    

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela - Quantidade de Commits por Membro\n\n")
            file.write("| Membro | Quantidade de Commits |\n")
            file.write("| --- | ---: |\n")
            for author, count in commit_count.items():
                file.write(f"| {author} | {count} |\n")
            file.write("\n")

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Commits por Autor\n\n")

            for author in commit_count.keys():
                file.write(f"## {author}\n\n")
                file.write("| Commit | Data |\n")
                file.write("| --- | --- |\n")
        
                author_commits = [commit for commit in self.commits if commit["commit"]["author"]["name"] == author]
        
                for commit in author_commits:
                    commit_message = commit["commit"]["message"]
                    commit_date = commit["commit"]["author"]["date"].split("T")[0]
                    commit_resume = " ".join(commit_message.split()[:7]) + "..." if len(commit_message.split()) > 7 else commit_message
                    file.write(f"| {commit_resume} | {commit_date} |\n")
                file.write("\n")
            file.write("\n")
