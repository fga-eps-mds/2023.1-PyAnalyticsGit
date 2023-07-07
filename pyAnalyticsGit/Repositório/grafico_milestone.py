import os
import matplotlib.pyplot as plt
from connect import Connect

class GraficoMilestone:
    def __init__(self):
        connect = Connect()
        self.milestones = connect.connect_milestone()
        self.issues = connect.connect_issue()

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
