import os
import pytest
from .repo.commit import Commits
from .repo.issue import Issue
from .repo.milestone import Milestone
from .repo.relatorio import Relatorio

diretorio_raiz = os.getcwd()
nome_pasta = "docs"
user= "fga-eps-mds"
repo= "2023.1-PyAnalyticsGit"
caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)

def test_gerar_nuvem_commits():
    try:
        grafico_nuvem = 'grafico_nuvem.png'
        obj  =  Commits(user,repo)
        obj.gerar_nuvem_commits()
        assert os.path.exists(os.path.join(caminho_pasta,grafico_nuvem))
    except Exception as e :
        pytest.fail(str(e))
 

def test_criar_grafico_commit():
    try:
        grafico = 'grafico.png'
        obj  =  Commits(user,repo)
        obj.criar_grafico_commit()
        assert os.path.exists(os.path.join(caminho_pasta,grafico))
    except Exception as e:
        pytest.fail(str(e))


def test_criar_grafico_pizza():
    try:
        obj = Issue(user,repo)
        obj.criar_grafico_pizza()
        assert os.path.exists(os.path.join(caminho_pasta,'grafico_pizza.png'))
    except Exception as e:
        pytest.fail(str(e))


def test_criar_grafico_issue():
    try:
        obj = Issue(user,repo)
        obj.criar_grafico_issue()
        assert os.path.exists(os.path.join(caminho_pasta,'grafico_issue.png'))
    except Exception as e:
        pytest.fail(str(e))


def test_criar_grafico_milestone():
    try:
        obj = Milestone(user,repo)
        obj.criar_grafico_milestones()
        assert os.path.exists(os.path.join(caminho_pasta,'grafico_milestone.png'))
    except Exception as e:
        pytest.fail(str(e))



def test_gerar_relatorio():
    try:
        obj = Relatorio()
        obj.gerar_relatorio(user,repo)
        assert os.path.exists(os.path.join(caminho_pasta,'relatorio_padrao.md'))
    except Exception as e:
        pytest.fail(str(e))
    