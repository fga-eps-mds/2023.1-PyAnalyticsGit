import os
from connect import Connect

class TabelaIssue:
    def __init__(self):
        connect = Connect()
        self.issues = connect.connect_issue()

    def criar_tabela_issue(self, relatorio_file):
        # Tabela de quantidade issues por autor
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
                file.write("| Issues | Tags |\n")
                file.write("| --- | --- |\n")
                for issue in self.issues:
                    if issue["user"]["login"] == author:
                        issue_title = issue['title']
                        tags = ', '.join(label['name'] for label in issue['labels'])
                        file.write(f"| {issue_title} | {tags} |\n")
                file.write("\n")
