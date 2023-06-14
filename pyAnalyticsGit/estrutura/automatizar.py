import subprocess
import os
import importlib.util
import sys

class automatizar:

    caminho_repositorio = ""
    path_biblioteca = ""
    localizacao_monitoramento = ""
    nome_biblioteca = "pyAnalyticsGit" #Classe que aciona o evento de monitoramento  

    def __init__(self):
        self.encontra_path_biblioteca()
        self.verifica_arquivo_git()
        self.automatiza_commit()

    @staticmethod
    def automatiza_commit():
        diretorio_hooks = f'{automatizar.caminho_repositorio}/hooks'
        #Path onde a biblioteca foi instalada
        comando_post_commit = f'''#!/bin/sh 
                                /usr/bin/python3 {automatizar.localizacao_monitoramento} '''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit.sh'

        print(f'Path .git/hooks: {diretorio_hooks}\n')
        print(f'comando_post_commit: {comando_post_commit}\n')
        print(f'Path post_commit: {diretorio_post_commit}\n')

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if comando_post_commit not in arquivo.read():
                arquivo.write(comando_post_commit)
            else:
                print('Arquivo post_commit não alterado.\n')

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    @staticmethod
    def verifica_arquivo_git():
        diretorio_atual = os.getcwd()   
        automatizar.caminho_repositorio = os.path.join(diretorio_atual, ".git")
        if os.path.exists(automatizar.caminho_repositorio):
            print(f'Path do repositório com .git: {automatizar.caminho_repositorio}\n')
            return automatizar.caminho_repositorio
        else:
            print("Arquivo .git do repositório não encontrado.\n")
        return None
    
    @staticmethod
    def acha_repositório():
        resultado = subprocess.run(['readlink', '-f',  __file__], capture_output=True, text=True)

        if resultado.returncode == 0:
            caminho_repositorio = resultado.stdout.strip()  #variavel chave
            #diretorio_atual = caminho_repositorio.rpartition('/')[0]
            print("Caminho do repositório:\n", caminho_repositorio) 
        return caminho_repositorio
    
    @staticmethod
    def encontra_path_biblioteca():
        try:
            spec = importlib.util.find_spec(automatizar.nome_biblioteca)
            if spec is not None:
                automatizar.path_biblioteca = spec.origin
                automatizar.localizacao_monitoramento = automatizar.path_biblioteca[:-11]
                automatizar.localizacao_monitoramento += "estrutura/monitoramento.py"
                print(f'Path da biblioteca: {automatizar.localizacao_monitoramento}\n')
                return automatizar.localizacao_monitoramento
            else:
                print('Path da biblioteca não encontrado.\n')
                return None
        except ImportError:
            return None  
