import requests
from dotenv import load_dotenv
import os
import sys
import datetime

diretorio_atual = os.getcwd()
arquivo_env = os.path.join(diretorio_atual,'.env')

api_user = ""
api_name = ""

load_dotenv(arquivo_env)

if os.path.exists(arquivo_env):
    api_user = os.getenv("user_name")
    api_name = os.getenv("repo_name")
else:
    print(f'Caso queira automatizar os commits insira o arquivo .env no diretório {diretorio_atual}')

class Connect:
    """Classe para conectar com a API do GitHub"""
    def __init__(self):
        pass

    def connect_issue(self, user = api_user, repo = api_name):
        """Método para conectar com a API do GitHub e obter as issues do repositório"""
        page = 1
        per_page = 100
        self.all_issues = []

        while True:           
            response = requests.get(f'https://api.github.com/repos/{user}/{repo}/issues?state=all&page={page}&per_page={per_page}')

            if response.status_code == 200:
                self.issues = response.json()
                self.all_issues.extend(self.issues)
                #print("conexão estabelecida\n")

                if len(self.issues) < per_page:
                    break
                else:
                    page += 1
            
            elif response.status_code == 403:
                print(f'StatusCode: {response.status_code}')
                print(f'Falha ao obter os detalhes do repositório {repo}. Foram feitas muitas requisições.')
                timestamp = response.headers['X-RateLimit-Reset']
                tempo_fora = datetime.datetime.fromtimestamp(int(timestamp))
                print(f'Você poderá voltar a fazer requisições em: {tempo_fora}')
                sys.exit()
    
            else:
                print(f'Falha ao obter os detalhes do repositório {repo}.')
                print(f'StatusCode: {response.status_code}')
                sys.exit()

        return self.all_issues       

    def connect_commit(self, user = api_user, repo = api_name):
        """Método para conectar com a API do GitHub e obter os commits do repositório"""
        page = 1
        per_page = 100
        self.all_commits = []

        while True:           
            response = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits?&all&page={page}&per_page={per_page}')

            if response.status_code == 200:
                self.commits = response.json()
                self.all_commits.extend(self.commits)
                #print("conexão estabelecida\n")

                if len(self.commits) < per_page:
                    break
                else:
                    page += 1
               
            elif response.status_code == 403:
                print(f'StatusCode: {response.status_code}')
                print(f'Falha ao obter os detalhes do repositório {repo}. Foram feitas muitas requisições.')
                timestamp = response.headers['X-RateLimit-Reset']
                tempo_fora = datetime.datetime.fromtimestamp(int(timestamp))
                print(f'Você poderá voltar a fazer requisições em: {tempo_fora}')
                sys.exit()

            else:
                print(f'Falha ao obter os detalhes do repositório {repo}.')
                print(f'StatusCode: {response.status_code}')
                sys.exit()

        return self.all_commits
    
    def connect_milestone(self, user = api_user, repo = api_name):
        """Método para conectar com a API do GitHub e obter os milestones do repositório"""
        url =f'https://api.github.com/repos/{user}/{repo}/milestones?state=all'
        response = requests.get(url)

        if response.status_code == 200:
            self.milestones = response.json()
            return self.milestones
        
        elif response.status_code == 403:
            print(f'StatusCode: {response.status_code}')
            print(f'Falha ao obter os detalhes do repositório {repo}. Foram feitas muitas requisições.')
            timestamp = response.headers['X-RateLimit-Reset']
            tempo_fora = datetime.datetime.fromtimestamp(int(timestamp))
            print(f'Você poderá voltar a fazer requisições em: {tempo_fora}')
            sys.exit()

        else:
            print(f'Falha ao obter os detalhes do repositório {repo}.\n')
            print(f'StatusCode: {response.status_code}')
            sys.exit()
