from collections import defaultdict
import os
import matplotlib.pyplot as plt
from connect import Connect
from issue import Issue

class GraficoPizza:
    def __init__(self):
        connect = Connect()
        self.issues = connect.connect_issue()

    def criar_grafico_pizza(self):
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
        if os.path.exists('pyAnalyticsGit/grafico_pizza.png'):
            os.remove('pyAnalyticsGit/grafico_pizza.png')   

        plt.savefig('pyAnalyticsGit/grafico_pizza.png')
        plt.show()

grafico_obj = GraficoPizza()
grafico_obj.criar_grafico_pizza()