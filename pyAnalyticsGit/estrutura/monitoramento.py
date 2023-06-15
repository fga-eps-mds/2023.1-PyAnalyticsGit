from Repositório.relatorio import Relatorio

class monitoramento:

  def rastreamento_git(self):
    """Quando algum commit for realizado este metodo é chamado. """
    print("------------------Um commit foi realizado.----------------------")
    obj = Relatorio()
    obj.exec_issues()
    obj.exec_milestones()
    
obj = monitoramento()
obj.rastreamento_git()
