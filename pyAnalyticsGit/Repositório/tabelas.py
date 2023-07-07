import os
from connect import Connect

class Tabelas:
    def __init__(self):
        connect = Connect()
        self.commits = connect.connect_commit()
        self.milestones = connect.connect_milestone()
        self.issues = connect.connect_issue()

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

    def criar_tabela_milestone(self, relatorio_file):
        milestone_issues = {}
        sprint_issues = {}

        for milestone in self.milestones:
            milestone_title = milestone["title"]
            milestone_issues[milestone_title] = 0
            sprint_issues[milestone_title] = []

        for issue in self.issues:
            issue_milestone = issue["milestone"]
            if issue_milestone:
                milestone_title = issue_milestone["title"]
                if milestone_title in milestone_issues:
                    milestone_issues[milestone_title] += 1
                    sprint_issues[milestone_title].append(issue["title"])

        with open(relatorio_file, "a+", encoding="utf-8") as file:
            file.write("# Tabela de Milestones e Issues\n\n")
            file.write("| Milestone | Número de Issues | Lista de Issues |\n")
            file.write("| --- | ---: | --- |\n")

            for milestone_title, issue_count in milestone_issues.items():
                issues_list = ", ".join(sprint_issues[milestone_title])
                file.write(f"| {milestone_title} | {issue_count} | {issues_list} |\n")

            file.write("\n")