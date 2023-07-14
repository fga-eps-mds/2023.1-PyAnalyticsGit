import subprocess
import os
import importlib.util
import platform
import sys

class Automatizar:
    """Realiza a configuração da automação gerando relatório a cada commit."""
    caminho_repositorio = str
    path_biblioteca = str
    localizacao_monitoramento = str
    nome_biblioteca = "pyanalyticsgit" 
    path_post_commit = str
    path_python = str
    comando_post_commit = str

    def __init(self):
        pass

    @staticmethod
    def automatiza():
        """Verifica o Sistema Operacional que está sendo utilizado."""
        sistema = platform.system()
        if sistema == 'Linux' or sistema == 'Darwin':
            Automatizar.automacao_unix()
        elif sistema == 'Windows':
            Automatizar.automacao_windows()
        else: 
            print('O sistema operacional não foi reconhecido!')
        
    @staticmethod
    def verifica_arquivo_git():
        """Verifica se o terminal que está executando é um repositório.
            Faz isso verificando a existência do arquivo .git no diretório."""
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
        """Encontra o path da biblioteca pyanalyticsgit e modifica gerando o path do módulo de monitoramento."""
        try:
            spec = importlib.util.find_spec(Automatizar.nome_biblioteca)
            Automatizar.path_biblioteca = spec.origin
            Automatizar.localizacao_monitoramento = Automatizar.path_biblioteca[:-11]
            Automatizar.localizacao_monitoramento += "monitoramento.py"
            print(f'Path da biblioteca: {Automatizar.localizacao_monitoramento}')
            return Automatizar.localizacao_monitoramento
        except ImportError:
            return None
        
    @staticmethod
    def encontra_path_python():
        """Encontra o path do python para ser adicionado a configuração da automação."""
        try:
            Automatizar.path_python = sys.executable
            print(f'Path Python: {Automatizar.path_python}\n')
            return Automatizar.path_python
        except ImportError:
            return None
        
    @staticmethod
    def automacao_unix():
        """Realiza a configuração da automação em sistemas baseados no Unix. 
            Este método ativa o módulo de monitoramanto por meio do evento post-commit do .git/hooks."""
        Automatizar.encontra_path_biblioteca()
        Automatizar.verifica_arquivo_git()
        Automatizar.encontra_path_python()
        diretorio_hooks = f'{Automatizar.caminho_repositorio}/hooks'
        Automatizar.comando_post_commit = f'''#!/bin/sh 
        {Automatizar.path_python} {Automatizar.localizacao_monitoramento}'''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        Automatizar.path_post_commit = diretorio_post_commit

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if Automatizar.comando_post_commit not in arquivo.read():
                arquivo.write(Automatizar.comando_post_commit)
                print("Configuração da Automação realizada com sucesso.\n")
            else:
                print('Configuração da automação não realizada!\n')

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    @staticmethod
    def automacao_windows():
        """Realiza a configuração da automação em sistemas Windows. 
            Este método ativa o módulo de monitoramanto por meio do evento post-commit do .git/hooks."""
        Automatizar.encontra_path_biblioteca()
        Automatizar.verifica_arquivo_git()
        Automatizar.encontra_path_python()
        diretorio_hooks = f'{Automatizar.caminho_repositorio}/hooks'
        #Path do Python
        Automatizar.comando_post_commit = f'''{Automatizar.path_python} {Automatizar.localizacao_monitoramento}'''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        Automatizar.path_post_commit = diretorio_post_commit

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if Automatizar.comando_post_commit not in arquivo.read():
                arquivo.write(Automatizar.comando_post_commit)
                print("Configuração da Automação realizada com sucesso.\n")
            else:
                print('Configuração da automação não realizada!\n')

        subprocess.run(['chmod', '+x', diretorio_post_commit])