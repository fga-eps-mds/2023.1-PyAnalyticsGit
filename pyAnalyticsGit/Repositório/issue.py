from connect import Connect

class Issue:
    def __init__(self):
        connect = Connect()
        self.all_issues = connect.connect_issue()

    def listar_issue(self):
        arq = open("relatorio_padrao.md","a+")
        arq.write('# Issues\n')
        for issue in self.all_issues:
            arq.seek(0)
            if str(issue["id"]) not in arq.read():
                arq.write(f'- Título: {issue["title"]}\n')
                arq.write(f'- Estado: {issue["state"]}\n')
                arq.write(f'- Número: {issue["number"]}\n')
                labels = []
                for label in issue["labels"]:
                    labels.append(label["name"])
                #arq.write("Labels:",", ".join(labels))
                arq.write(f'- Labels: {", ".join(labels)}\n')
                arq.write('---------------------\n')

    def listar_issue_label(self,label):
        arq = open(f'issues_{label}.md',"w+")
        arq.write(f'### Todas as issues de **{label}:**\n\n')
        c = 0
        for issue in self.all_issues:
            for labels in issue["labels"]:
                if labels["name"] == label:
                    arq.write(f'- Título: {issue["title"]}\n')
                    arq.write(f'- Estado: {issue["state"]}\n')
                    arq.write(f'- Número: {issue["number"]}\n')
                    arq.write('---------------------\n')
                    c = c + 1
        if c == 0 :
            print("Label não encontrada")
        else:
            print(c)          

    def contador_issues(self):
        contador = {}
        for issue in self.all_issues:
            labels = []
            for label in issue["labels"]:
                labels.append(label["name"])
        
            for rotulo in labels:
                if rotulo in contador:
                    contador[rotulo] += 1
                else:
                    contador[rotulo] = 1
        
        labels_ordenada = sorted(contador.items(), key= lambda x:x[1], reverse=True)

        with open("teste.md","a+") as arq:
            arq.write("## Teste de contagem de Issues\n\n")
            for rotulo,count in labels_ordenada:
                arq.write(f'- **{rotulo}**: ')
                arq.write(f'{str(count)}\n')
                    


#issue1 = Issue()
#issue1.listar_issue()
#issue2.connect("fga-eps-mds","2023.1-PyAnalyticsGit")
#issue2.listar_issue_label("documentation")
#issue2.listar_issue()