import requests

class Connect:
    def __init__(self):
        pass
    

    def connect_issue(self,username,reponame):
        self.username = username
        self.reponame = reponame

        page = 1
        per_page = 30
        self.all_issues = []

        while True:           
            response = requests.get(f'https://api.github.com/repos/{username}/{reponame}/issues?state=all&page={page}&per_page={per_page}')

            if response.status_code == 200:
                self.issues = response.json()
                self.all_issues.extend(self.issues)
                #print("conexão estabelecida\n")

                if len(self.issues) < per_page:
                    break
                else:
                    page += 1
               

            else:
                print(f'Falha ao obter os detalhes do repositório {reponame}.')
                print(f'StatusCode: {response.status_code}')
                break

        return self.all_issues       

# connect = Connect()

# all_issues  = connect.connect_issue("fga-eps-mds","2023.1-PyAnalyticsGit")
# print(all_issues)