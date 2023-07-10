from relatorio import Relatorio
from connect import Connect
from dotenv import load_dotenv

class monitoramento:

  def rastreamento_git(self):
    """Quando algum commit for realizado este metodo é chamado. """
    print("------------------Um commit foi realizado.----------------------")
    obj = Relatorio()
    #obj.exec_issues()
    #obj.exec_milestones()
    #obj.exec_commits()
    obj.gerar_relatorio()

obj = monitoramento()
obj.rastreamento_git()
