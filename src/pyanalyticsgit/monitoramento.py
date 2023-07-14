# from relatorio import Relatorio
from repo.relatorio import Relatorio

class monitoramento:
  def rastreamento_git(self):
    """Módulo que gera o relatório automatizado. Acionado pelo evento de commit."""
    obj = Relatorio()
    obj.gerar_relatorio()

obj = monitoramento()
obj.rastreamento_git()
