from .repo.automatizar import Automatizar
from pathlib import Path

def test_encontra_path_biblioteca_windows(monkeypatch):
    teste_path = Automatizar.encontra_path_biblioteca()
    resultado = Automatizar.encontra_path_biblioteca()
    assert resultado == teste_path

def test_verifica_arquivo_git_windows(monkeypatch):
    test_git = Automatizar.verifica_arquivo_git()
    resultado = Automatizar.verifica_arquivo_git()
    assert resultado == test_git

def test_automatiza_commit_windows():
    arquivo_hooks = f'{Automatizar.verifica_arquivo_git()}/hooks/post-commit'
    comando = f'''{Automatizar.encontra_path_python()} {Automatizar.encontra_path_biblioteca()}'''
    resultado = Automatizar()
    resultado.automacao_windows()
    assert resultado.path_post_commit == arquivo_hooks
    assert resultado.comando_post_commit == comando