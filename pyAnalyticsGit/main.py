"""
    Teste de criação do relatório markdown a partir do algoritmo.
    Implementação inicial de teste dos commits e gráfico que analisa 
    a quantidade de commits por integrante.
"""
from git import Repo, Commit
import matplotlib.pyplot as plt
import subprocess

contador_commit = 0

#Variavel que guarda o caminho do repositorio(Trocar para o caminho do seu PC)
repo_path = "/home/jefferson/UnB/Mds/Projeto_Mds/2023.1-Biblioteca-Relatorios-Git" 

repo = Repo(repo_path) 

commits = list(repo.iter_commits('main'))

def grafico():
# Dicionário para armazenar o número de commits por usuário
    commits_por_usuario = {
        'PedroHhenriq': 0,
        'Gabriel': 0,
        'Tiago1604': 0,
        'JeffersonSenaa': 0,
        'rodfon3301': 0,
        'mateus9Levy': 0
    }

    # Contador para o número de commits por integrante
    for commit in commits:
        name = commit.author.name
        if name in commits_por_usuario:
            commits_por_usuario[name] += 1

    usuarios = list(commits_por_usuario.keys())
    num_commits = list(commits_por_usuario.values())

    plt.bar(usuarios, num_commits, color='green')
    plt.title("Média de commits por integrante")
    plt.xlabel("Integrantes")
    plt.ylabel("Commits")
    plt.savefig('pyAnalyticsGit/grafico_commits.png')

    code_md = "![Gráfico de Commits](grafico_commits.png)" 

    subprocess.run(f"echo '{code_md}' >> pyAnalyticsGit/infos_commit.md", shell=True)

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
