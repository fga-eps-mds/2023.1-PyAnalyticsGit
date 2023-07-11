import os
import matplotlib.pyplot as plt
import pytest
from .commit import Commits



diretorio_raiz = os.getcwd()
nome_pasta = "docs"
grafico = 'grafico.png'
grafico_nuvem = 'grafico_nuvem.png'
caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)

def test_gerar_nuvem_commits():
    obj  =  Commits()
    try:
        obj.gerar_nuvem_commits()
        assert os.path.exists(os.path.join(caminho_pasta,grafico_nuvem))
    except Exception as e :
        pytest.fail(str(e))

def test_criar_grafico_commit():
    obj = Commits()
    try:
        obj.criar_grafico_commit()
        assert os.path.exists(os.path.join(caminho_pasta,grafico_nuvem))
    except Exception as e:
        pytest.fail(str(e))