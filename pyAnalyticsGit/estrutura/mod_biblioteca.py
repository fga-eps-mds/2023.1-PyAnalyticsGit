import subprocess
class mod_biblioteca:
    
    @staticmethod
    def automatiza_commit():
        """Metodo que por meio do subprocess altera o post-commit para que seja automatizado os commits."""
        diretorio_hooks = "/home/jefferson/unb/mds/projeto_mds/RepositorioTest/repositorioTestPyAnalytics/.git/hooks"

        comando_post_commit = '''#!/bin/sh
            echo "Commit realizado!"
            python unb/mds/projeto_mds/2023.1-PyAnalyticsGit/pyAnalyticsGit/estrutura/monitoramento.py '''

        diretorio_post_commit = f'{diretorio_hooks}/post-commit'

        with open (diretorio_post_commit, 'a+') as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro de leitura no início do arquivo
            if comando_post_commit not in arquivo.read():
                arquivo.write(comando_post_commit)

        subprocess.run(['chmod', '+x', diretorio_post_commit])

    automatiza_commit()
