class relatorio:
    def __init__(self):
        self.nome_arquivo = "relatorio_padrao.md"
        self.titulo = "## PyAnalyticsGit - Relatório automatizado"
        with open(self.nome_arquivo, 'a+') as arq:
            arq.seek(0)
            if self.titulo not in arq.read():
                arq.write(f'{self.titulo}\n')

template = relatorio()
