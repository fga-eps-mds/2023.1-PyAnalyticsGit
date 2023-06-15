from datetime import datetime
from connect import Connect 



class Milestone:
    def __init__(self):
        connect = Connect()
        self.milestones = connect.connect_milestone()

    def list_milestone(self):
        arq = open(f'relatorio_padrao.md','a+')
        arq.write('# Milestones\n')
        for milestone in self.milestones:
            data_inicio = milestone["created_at"]
            data_formatada = datetime.strptime(data_inicio, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
            arq.write(f'- Título: {milestone["title"]}\n')
            arq.write(f'- Cirado em: {data_formatada}\n')
            arq.write(f'- Descrição: {milestone["description"]}\n')
            arq.write(f'- Issues Abertas: {milestone["open_issues"]}\n')
            arq.write(f'- Issues Fechadas: {milestone["closed_issues"]}\n')
            arq.write('---------------------\n')

