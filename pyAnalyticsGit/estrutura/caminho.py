import subprocess

def acha_repositório():
    resultado = subprocess.run(['readlink', '-f',  __file__], capture_output=True, text=True)

    if resultado.returncode == 0:
        caminho_repositorio = resultado.stdout.strip()  #variavel chave
        #diretorio_atual = caminho_repositorio.rpartition('/')[0]
        print("Caminho do repositório:", caminho_repositorio) 
    return caminho_repositorio

acha_repositório()
