import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_user = os.getenv("user_name")
api_name = os.getenv("repo_name")

class Connect:
    def __init__(self):
        pass

    def connect_issue(self, user = api_user, repo = api_name):
        page = 1
        per_page = 30
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
               

            else:
                print(f'Falha ao obter os detalhes do repositório {repo}.')
                print(f'StatusCode: {response.status_code}')
                print(response.status_code)
                x_rate_limit_reset = response.headers['X-RateLimit-Reset']
                print(x_rate_limit_reset)
                break

        return self.all_issues       

    def connect_commit(self, user = api_user, repo = api_name):
        page = 1
        per_page = 30
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
               

            else:
                print(f'Falha ao obter os detalhes do repositório {repo}.')
                print(f'StatusCode: {response.status_code}')
                break

        return self.all_commits
    
    def connect_milestone(self, user = api_user, repo = api_name):
        url =f'https://api.github.com/repos/{user}/{repo}/milestones?state=all'
        response = requests.get(url)

        if response.status_code == 200:
            self.milestones = response.json()
            return self.milestones
        else:
            print(f'Falha ao obter os detalhes do repositório {repo}.\n')
            print(f'StatusCode: {response.status_code}')

