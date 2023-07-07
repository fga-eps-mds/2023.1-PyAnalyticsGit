from connect import Connect

class TabelaMilestone:
    def __init__(self):
        connect = Connect()
        self.milestones = connect.connect_milestone()
        self.issues = connect.connect_issue()

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