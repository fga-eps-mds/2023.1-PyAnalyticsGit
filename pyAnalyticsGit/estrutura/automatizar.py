import subprocess
import os
import importlib.util
import sys

class automatizar:

    caminho_repositorio = None
    localizacao_monitoramento = None
    nome_biblioteca = "monitoramento" #Classe que aciona o evento de monitoramento  

    @staticmethod
    def automatiza_commit():
        diretorio_hooks = f'{automatizar.caminho_repositorio}/hooks'
        #Path onde a biblioteca foi instalada
        comando_post_commit = f'#!/bin/sh /usr/bin/python3 {automatizar.localizacao_monitoramento} '

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        print(f'Teste: - diretorio_hooks: {diretorio_hooks}\n')
        print(f'Teste: - comando_post_commit: {comando_post_commit}\n')
        print(f'Teste: - diretorio_post_commit: {diretorio_post_commit}\n')

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if comando_post_commit not in arquivo.read():
                arquivo.write(comando_post_commit)
            else:
                print('Arquivo não alterado!---')

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    """
        Este metodo verifica se o arquivo .git está na pasta onde o arquivo de import
        da biblioteca será executado. 
        O comando os.getcwd() retorna o caminho de execução do método. Em seguida é
        adicionado o .git ao caminho para verificar sua existência.
    """
    @staticmethod
    def verifica_arquivo_git():
        diretorio_atual = os.getcwd()   
        automatizar.caminho_repositorio = os.path.join(diretorio_atual, ".git")
        if os.path.exists(automatizar.caminho_repositorio):
            print("Caminho do repositório:\n", automatizar.caminho_repositorio)
            return automatizar.caminho_repositorio
        else:
            print("Arquivo .git do repositório não encontrado.")
        return None
    
    @staticmethod
    def acha_repositório():
        resultado = subprocess.run(['readlink', '-f',  __file__], capture_output=True, text=True)

        if resultado.returncode == 0:
            caminho_repositorio = resultado.stdout.strip()  #variavel chave
            #diretorio_atual = caminho_repositorio.rpartition('/')[0]
            print("Caminho do repositório:\n", caminho_repositorio) 
        return caminho_repositorio
    
    #Encontra o path onde a biblioteca foi instalada
    #sys.prefix retorna o diretório onde o python esta sendo executado
    #importlib e sys são modulos nativos do python
    #Se for declarado no caminho "site-packages a biblioteca está em um ambiente virtual"
    @staticmethod
    def encontra_path_biblioteca():
        try:
            spec = importlib.util.find_spec(automatizar.nome_biblioteca)
            if spec is not None:
                automatizar.localizacao_monitoramento = spec.origin
                print(f'O metodo retornou: {automatizar.localizacao_monitoramento}\n')
                return automatizar.localizacao_monitoramento
            else:
                print('Caminho não encontrado')
                return None
        except ImportError:
            return None    

#Teste de Implementação
obj = automatizar()
obj.encontra_path_biblioteca()
obj.verifica_arquivo_git()
obj.automatiza_commit()

