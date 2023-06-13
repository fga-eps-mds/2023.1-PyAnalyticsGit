import subprocess
import os

class mod_biblioteca:

    caminho_repositorio = None

    @staticmethod
    def automatiza_commit():
        diretorio_hooks = f'{mod_biblioteca.caminho_repositorio}/hooks'

        #Path onde a biblioteca foi instalada
        comando_post_commit = '''#!/bin/sh
            /usr/bin/python3 /home/jefferson/unb/mds/projeto_mds/2023.1-PyAnalyticsGit/pyAnalyticsGit/estrutura/monitoramento.py '''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if comando_post_commit not in arquivo.read():
                arquivo.write(comando_post_commit)
            else:
                print('Arquivo não alterado!---')

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    @staticmethod
    def verifica_arquivo_git():
        #Verifica se o arquivo .git esta no path e salva o caminho
        diretorio_atual = os.getcwd()   
        mod_biblioteca.caminho_repositorio = os.path.join(diretorio_atual, ".git")
        
        if os.path.exists(mod_biblioteca.caminho_repositorio):
            print("Caminho do repositório:", mod_biblioteca.caminho_repositorio)
            return mod_biblioteca.caminho_repositorio
        else:
            print("Arquivo .git do repositório não encontrado.")
        return None
    
    @staticmethod
    def acha_repositório():
        resultado = subprocess.run(['readlink', '-f',  __file__], capture_output=True, text=True)

        if resultado.returncode == 0:
            caminho_repositorio = resultado.stdout.strip()  #variavel chave
            #diretorio_atual = caminho_repositorio.rpartition('/')[0]
            print("Caminho do repositório:", caminho_repositorio) 
        return caminho_repositorio
    

obj = mod_biblioteca()
obj.acha_repositório()
obj.verifica_arquivo_git()
