from relatorio import Relatorio
from pyAnalyticsGit.analyticsgit.connect import Connect
from dotenv import load_dotenv

class monitoramento:

  def rastreamento_git(self): 
    obj = Relatorio()
    obj.gerar_relatorio()

obj = monitoramento()
obj.rastreamento_git()
