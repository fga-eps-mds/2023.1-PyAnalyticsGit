import subprocess
import os
import importlib.util
import platform
import sys

class Automatizar:
    caminho_repositorio = str
    path_biblioteca = str
    localizacao_monitoramento = str
    nome_biblioteca = "pyAnalyticsGit" 
    path_post_commit = str
    path_python = ""
    comando_post_commit = str

    def __init(self):
        pass

    @staticmethod
    def automatiza():
        sistema = platform.system()
        if sistema == 'Linux' or sistema == 'Darwin':
            Automatizar.automacao_unix()
        elif sistema == 'Windows':
            Automatizar.automacao_windows()
        else: 
            print('O sistema operacional não foi reconhecido!')
        
    @staticmethod
    def verifica_arquivo_git():
        diretorio_atual = os.getcwd()   
        Automatizar.caminho_repositorio = os.path.join(diretorio_atual, ".git")
        if os.path.exists(Automatizar.caminho_repositorio):
            print(f'Arquivo Git: {Automatizar.caminho_repositorio}')
            return Automatizar.caminho_repositorio
        else:
            print("Arquivo .git do repositório não encontrado.\n")
            return None
    
    @staticmethod
    def encontra_path_biblioteca():
        try:
            spec = importlib.util.find_spec(Automatizar.nome_biblioteca)
            Automatizar.path_biblioteca = spec.origin
            Automatizar.localizacao_monitoramento = Automatizar.path_biblioteca[:-11]
            Automatizar.localizacao_monitoramento += "monitoramento.py"
            print(f'Path da biblioteca: {Automatizar.localizacao_monitoramento}\n')
            return Automatizar.localizacao_monitoramento
        except ImportError:
            return None
        
    @staticmethod
    def encontra_path_python():
        try:
            Automatizar.path_python = sys.executable
            print(f'Path Python: {Automatizar.path_python}')
            return Automatizar.path_python
        except ImportError:
            return None
        
    @staticmethod
    def automacao_unix():
        Automatizar.encontra_path_biblioteca()
        Automatizar.verifica_arquivo_git()
        diretorio_hooks = f'{Automatizar.caminho_repositorio}/hooks'
        Automatizar.comando_post_commit = f'''#!/bin/sh 
        {Automatizar.path_python} {Automatizar.localizacao_monitoramento}'''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        Automatizar.path_post_commit = diretorio_post_commit

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if Automatizar.comando_post_commit not in arquivo.read():
                arquivo.write(Automatizar.comando_post_commit)
                print("O arquivo post-commit foi alterado\n")
            else:
                print('Arquivo post_commit não alterado.\n')

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    @staticmethod
    def automacao_windows():
        Automatizar.encontra_path_biblioteca()
        Automatizar.verifica_arquivo_git()
        diretorio_hooks = f'{Automatizar.caminho_repositorio}/hooks'
        #Path do Python
        Automatizar.comando_post_commit = f'''{Automatizar.path_python} {Automatizar.localizacao_monitoramento}'''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        Automatizar.path_post_commit = diretorio_post_commit

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if Automatizar.comando_post_commit not in arquivo.read():
                arquivo.write(Automatizar.comando_post_commit)
                print("O arquivo post-commit foi alterado\n")
            else:
                print('Arquivo post_commit não alterado.\n')

        subprocess.run(['chmod', '+x', diretorio_post_commit])