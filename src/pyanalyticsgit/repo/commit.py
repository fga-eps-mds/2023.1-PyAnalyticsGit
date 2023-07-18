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

        plt.figure(figsize=(14, 8))
        plt.imshow(wordcloud, interpolation='bilinear') 
        plt.axis('off')
        plt.title('Nuvem de palavras com nomes dos Commits')

        if os.path.exists(os.path.join(caminho_pasta,grafico_nuvem)):
            os.remove(os.path.join(caminho_pasta,grafico_nuvem))

        plt.savefig(os.path.join(caminho_pasta,grafico_nuvem))
        plt.close()    

    def criar_grafico_commit(self):
        """Método que cria um gráfico de barras com os nomes dos autores e a quantidade de commits"""
        authors = {}
        for commit in self.commits:
            author_name = commit['commit']['author']['name']
            author_login = commit['author']['login'] if commit['author'] is not None else ""

            # Usa o nome do autor como chave para agrupar os commits
            key = author_name.lower()
            if key not in authors:
                authors[key] = {
                    'name': author_name,
                    'login': author_login,
                    'count': 1
                }
            else:
                authors[key]['count'] += 1

        nicknames = [author['login'] for author in authors.values()]
        commit_counts = [author['count'] for author in authors.values()]

        plt.figure(figsize=(8, 9))
        plt.bar(nicknames, commit_counts, color='darkred')
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
        authors = {}
        for commit in self.commits:
            author_name = commit['commit']['author']['name']
            author_login = commit['author']['login'] if commit['author'] is not None else ""

            if author_login not in authors:
                authors[author_login] = {
                    'name': author_login,
                    'commits': [],
                    'count': 1
                }
            else:
                authors[author_login]['count'] += 1

            authors[author_login]['commits'].append(commit)

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela - Quantidade de Commits por Autor\n\n")
            file.write("| Autor | Quantidade de Commits |\n")
            file.write("| --- | ---: |\n")
            for author_login, data in authors.items():
                file.write(f"| {data['name']} | {data['count']} |\n")
            file.write("\n")

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            for author_login, data in authors.items():
                file.write("# Tabela de Commits por Autor\n\n")
                file.write(f"## {data['name']}\n\n")
                file.write("| Commit | Data |\n")
                file.write("| --- | --- |\n")

                for commit in data['commits']:
                    commit_message = commit["commit"]["message"]
                    commit_date = commit["commit"]["author"]["date"].split("T")[0]
                    commit_resume = " ".join(commit_message.split()[:7]) + "..." if len(commit_message.split()) > 7 else commit_message
                    file.write(f"| {commit_resume} | {commit_date} |\n")
                file.write("\n")