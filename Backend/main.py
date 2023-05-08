"""
    Teste de interação da Biblioteca por meio da Biblioteca GitPython.
    Essa interação é feita utilizando os comandos da biblioteca.
    Primeiros testes da implementação/testando
"""
from git import Repo, Commit
import matplotlib.pyplot as plt

#COMMITS_TO_PRINT = 20
contador_commit = 0

#Variavel que guarda o caminho do repositorio(Trocar para o caminho do seu PC)
repo_path = "/home/tiago/Documentos/clonando/2023.1-Biblioteca-Relatorios-Git" 

#Variavel que chama o repositorio
repo = Repo(repo_path) 

#commits = list(repo.iter_commits())
commits = list(repo.iter_commits('main'))#[:COMMITS_TO_PRINT]

def grafico():
    name = list()
    usuario = 0
    usuario1 = 0
    usuario2 = 0
    usuario3 = 0
    usuario4 = 0
    usuario5 = 0
    for commit in commits:
        name = commit.author.name
        if name == 'PedroHhenriq':
            usuario += 1
        elif name == 'Gabriel':
            usuario1 += 1
        elif name == 'Tiago1604':
            usuario2 += 1
        elif name == 'JeffersonSenaa':
            usuario3 += 1
        elif name == 'rodfon3301':
            usuario4 += 1
        elif name == 'mateus9Levy':
            usuario5 += 1

    y = [usuario, usuario1, usuario2, usuario3, usuario4, usuario5]
    x = ['Pedro', 'Gabriel', 'Tiago', 'Jefferson', 'Rodrigo', 'Mateus']

    plt.bar(x,y)
    plt.title("Média de commit's por integrante")
    plt.xlabel("Integrantes")
    plt.ylabel("Commit's")
    plt.bar(x,y, color='green')
    #plt.show()
    #plt.savefig('Backend/grafico_commits.png')

    code_md = "![Gráfico de Commits](grafico_commits.png)" 

    subprocess.run(f"echo '{code_md}' >> Backend/relatorio.md", shell=True)


def commit(nome_arquivo, qtd_commits):
    global contador_commit
    global commits
    commits = commits[:qtd_commits]
    if not repo.bare:
        print(f'O repositório {repo_path} foi carregado com sucesso!')
        arq = open(f'{nome_arquivo}.md','w+')
        for count in commits:
            contador_commit = contador_commit + 1
        arq.write(f'**Número Total de commits: {contador_commit}**\n')
        arq.write('\n')
        arq.write('**Informação dos commits:**\n')    
        for commit in commits:
            arq.write('----------------------------------------------------------------------------------\n')
            arq.write(f'- impressão do hash: {commit.hexsha}\n')
            arq.write(f'- Mensagem do Commit: {commit.message}\n')
            arq.write(f'- Autor: {commit.author.name} | e-mail: ({commit.author.email})\n')
            arq.write(f'- {commit.authored_datetime}')
            arq.write('\n')
            arq.write(f'- Número do Commit: {commit.count()}\n')
            arq.write('\n')
            #contador_commit = contador_commit + 1
            pass
        #arq.write(f'**Número Total de commits: {contador_commit}**')
    else:
        print(f'Não foi possivel encontrar uma repositório em uso em {repo_path}')


grafico()
commit('infos_commit',25)
