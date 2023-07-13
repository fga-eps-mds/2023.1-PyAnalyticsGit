from collections import defaultdict
import matplotlib.pyplot as plt
import os
from .connect import Connect,api_name,api_user

# diretorio_raiz = os.path.abspath(os.path.dirname(__file__))
diretorio_raiz = os.getcwd()


nome_pasta = "docs"
grafico_issue = 'grafico_issue.png'
grafico_pizza = 'grafico_pizza.png'

caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)

class Issue:
    """Classe para gerar gráficos e tabelas de issues"""
    def __init__(self, user = api_user, repo = api_name):
        """Construtor da classe Issue"""
        connect = Connect()
        self.issues = connect.connect_issue(user,repo)
        self.nome_arquivo = 'relatorio_padrao.md'
        self.caminho_arquivo = os.path.join(caminho_pasta,self.nome_arquivo)

    def criar_grafico_pizza(self):
        """Método que cria um gráfico de pizza com as tags das issues"""
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
        if os.path.exists(os.path.join(caminho_pasta,grafico_pizza)):
            os.remove(os.path.join(caminho_pasta,grafico_pizza))   

        plt.savefig(os.path.join(caminho_pasta,grafico_pizza))
        plt.close()

    def criar_grafico_issue(self):
        """Método que cria um gráfico de barras com a quantidade de issues por autor"""
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
        if os.path.exists(os.path.join(caminho_pasta,grafico_issue)):
            os.remove(os.path.join(caminho_pasta,grafico_issue))

        plt.savefig(os.path.join(caminho_pasta,grafico_issue))
        plt.close()

    def criar_tabela_issue(self, relatorio_file):
        """Método que cria uma tabela com as issues por autor"""
        issue_count = {}
        for issue in self.issues:
            author = issue["user"]["login"]
            if author in issue_count:
                issue_count[author] += 1
            else:
                issue_count[author] = 1

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Quantidade de Issues por Autor\n\n")
            file.write("| Autor | Quantidade de Issues |\n")
            file.write("| --- | ---: |\n")
            for author, count in issue_count.items():
                file.write(f"| {author} | {count} |\n")
            file.write("\n")

        # Tabela de issues por autor
        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Issues por Autor com Tags\n\n")
            for author in issue_count.keys():
                file.write(f"## {author}\n\n")
                file.write("| Título | Número | Estado | Tags |\n")
                file.write("| --- | --- | --- | --- |\n")
                for issue in self.issues:
                    if issue["user"]["login"] == author:
                        issue_title = issue['title']
                        issue_number = issue['number']
                        issue_state = issue['state']
                        tags = ', '.join(label['name'] for label in issue['labels'])
                        file.write(f"| {issue_title} | {issue_number} | {issue_state} | {tags} |\n")
                file.write("\n")   