"""
    Teste de interação da Biblioteca por meio da Biblioteca GitPython.
    Essa interação é feita utilizando os comandos da biblioteca.
    Primeiros testes da implementação/testando
"""
from git import Repo, Commit
import matplotlib.pyplot as plt

#COMMITS_TO_PRINT = 5

#Variavel que guarda o caminho do repositorio
repo_path = "/home/jefferson/UnB/Mds/Projeto_Mds/2023.1-Biblioteca-Relatorios-Git" 

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
    plt.show()

def commit():
    if not repo.bare:
        print(f'O repositório {repo_path} foi carregado com sucesso!')
        for commit in commits:
            print('----------------------------------------------------------------------------------')
            print(f'impressão do hash:{commit.hexsha}')
            print(f'Mensagem do Commit: {commit.message}')
            print(f'{commit.summary} by {commit.author.name} by ({commit.author.email})')
            print(str(commit.authored_datetime))
            print(f'Número do Commit: {commit.count()}')
            pass
    else:
        print(f'Não foi possivel encontrar uma repositório em uso em {repo_path}')

grafico()
commit()
