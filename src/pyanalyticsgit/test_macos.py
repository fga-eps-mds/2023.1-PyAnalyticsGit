from .repo.automatizar import Automatizar
from pathlib import Path

def test_encontra_path_biblioteca(monkeypatch):
    teste_path = "/Users/runner/work/2023.1-PyAnalyticsGit/2023.1-PyAnalyticsGit/pyAnalyticsGit/monitoramento.py"
    def mock_home():
        return Path(teste_path)
    monkeypatch.setattr(Path, "home", mock_home)
    resultado = Automatizar.encontra_path_biblioteca()
    assert resultado == teste_path


def test_verifica_arquivo_git(monkeypatch):
    teste_git = "/Users/runner/work/2023.1-PyAnalyticsGit/2023.1-PyAnalyticsGit/.git"
    def mock_home():
        return Path(teste_git)
    monkeypatch.setattr(Path, "home", mock_home)
    resultado = Automatizar.verifica_arquivo_git()
    assert resultado == teste_git

def test_automatiza_commit_unix():
    arquivo_hooks = f'{Automatizar.verifica_arquivo_git()}/hooks/post-commit'
    comando = f'''#!/bin/sh 
        {Automatizar.encontra_path_python()} {Automatizar.encontra_path_biblioteca()}'''
    resultado = Automatizar()
    resultado.automacao_unix()
    assert resultado.path_post_commit == arquivo_hooks
    assert resultado.comando_post_commit == comando