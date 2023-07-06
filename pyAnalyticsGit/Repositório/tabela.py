import os
from connect import Connect

class Tabela:
    def __init__(self):
        connect = Connect()
        self.commits = connect.connect_commit()

    def criar_tabela(self, relatorio_file):
        # Tabela de quantidade de commits por membro
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

        # Tabela de commits por membro
        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Commits por Membro\n\n")
            for author in commit_count.keys():
                file.write(f"## {author}\n\n")
                file.write("| Commits | Data |\n")
                file.write("| --- | --- |\n")
                commits = commit_datas[author]
                for i in range(len(commits)):
                    commit_date = commits[i].split("T")[0]
                    file.write(f"| {self.commits[i]['commit']['message']} | {commit_date} |\n")
                file.write("\n")
               
