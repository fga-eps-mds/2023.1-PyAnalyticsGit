"""
    Teste de interação da Biblioteca por meio da Biblioteca GitPython.
    Essa interação é feita utilizando os comandos da biblioteca.
    Primeiros testes da implementação/testando
"""
from git import Repo, Commit

COMMITS_TO_PRINT = 5

#Variavel que guarda o caminho do repositorio
repo_path = "/home/tiago/Documentos/Curso Python/fsp" 

#Variavel que chama o repositorio
repo = Repo(repo_path) 


#commits = list(repo.iter_commits())
commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]

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
