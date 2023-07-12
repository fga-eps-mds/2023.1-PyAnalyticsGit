<div align="center">
<img src="https://user-images.githubusercontent.com/98030427/236968066-315be92b-eabe-4d76-a5d7-bbaaa8df1e2d.png" width="78px" />
</div>




# 📝 Descrição
O PyAnalyticsGit é um projeto em Python criado por estudantes de Engenharia de Software que tem como funcionalidades, a biblioteca do PyAnalyticsGit possibilita que o usuário consiga gerar relatórios automatizados com base em dados de repositórios do GitHub, tais quais, histórico de commits, nome do commit, branch, tamanho do log, etc...

A biblioteca do PyAnalyticsGit deve ser capaz de analisar o desempenho de um projeto oferecendo no relatório parâmetros como taxa de commit por branch, taxa de commit por tempo, horario recorrente de commit, entre outros.

Com essa ferramenta, é possível obter uma ampla variedade de dados e análises de projetos e repositórios do Git, incluindo gráficos e estatísticas. A biblioteca funciona recebendo os dados de saída dos comandos do Git e realizando a análise e tratamento dos dados de forma eficiente e precisa. Com essa solução, os usuários podem otimizar seus processos e aprimorar a gestão dos seus projetos do Git.

## :dart: Objetivo
### Qual é o propósito do PyAnalyticsGit?

O PyAnalyticsGit tem como objetivo geral fornecer  uma forma automatizada, eficiente e acessível de gerar relatórios com informações de projetos, progressos e as métricas com dados de repositórios no Github, afim de acompanhar e ter o controle do andamento daquele projeto. Desta forma, os principais objetivos que do PyAnalyticsGit é:

* Extrair informações relevantes de commits, issues e milestones do GitHub.
* Gerar relatórios em formato Markdown para facilitar a leitura e compartilhamento.
* Incluir gráficos e tabelas para apresentar visualmente as informações extraídas.
* Facilitar o acompanhamento do desenvolvimento do projeto e a tomada de decisões.

##

## Fluxo de Instalação e Funcionamento
***OBS: Os comandos estão configurados em Linux, mas deverá estar para Linux,
MacOs e Windows***


### Instalação/Introdução
 Breve Descrição da API e da Biblioteca (Funcionamento e Visão de Produto
Resumido). Inicialmente, é recomendável a utilização de um ambiente virtual, que pode ser
criado através do venv:

Digite em seu terminal:
```
python3 -m venv myenv
```
Pronto, Assim sera criado um ambiente virtual chamado "myenv"

Para ativar o ambiente:
```
source myenv/bin/activate
```
Agora que o ambiente virtual está devidamente criado, Verifique se o ambiente foi inicializado corretamente (verifique que se o nome
do ambiente, nesse caso “myenv” está no início do caminho em seu terminal.

### Instalação da biblioteca
Vamos começar a instalar a biblioteca com o seguinte comando:
- Instale o sistema de gerenciamento de bibliotecas python “pip”
- Execute o comando em seu terminal:
```
pip install pyanalyticsgit
```
- Para verificar se a instalação ocorreu com sucesso execute em seu
terminal:
```
pip show pyanalyticsgit
```
### Automação
Apos a configurado e instalado agora o usuario configura a automação. 

O usuário deve executar o arquivo a partir de diretório que contenha .git (de um
diretório que é repositório)

Para verificar se seu diretório é um repositório verifique se tem o arquivo
“.git”
- execute no terminal o comando: ls -a (pois o .git é uma pasta oculta) —
(verificar como é no windows)

Verificado isso deve importar a classe Automatiza:
```
from analyticsgit.automatiza import Automatiza
```
Após importar deve chamar o método automatiza():
```
Automatizar.automatiza()
```
Este método verifica qual o SO utilizado e
cria o arquivo post-commit para automatizar


Ao executar o repositório estará automatizado e a cada commit será gerado um
relatório.
Após executar o método de automação não é necessário executar novamente.
O usuário deve apagar o método caso for gerar um relatório Estático.

### Relatório Automatizado

A cada evento de commit o git chama o método de monitoramento que executa
a criação do relatório.
- Obs: Toda essa parte é automatizada o usuário so precisa executar os
métodos de cima e configurar o .env

O relatório gerado estará em um arquivo docs/relatorio.md

- .env:
  - Deve ser criado um arquivo .env no ambiente de utilização da biblioteca e
definir os valores de ‘user_name’(usuário ou repositório que contém o
repositório que se quer o relatório) e ‘repo_name’ (repositório desejado)
  - Exemplo no repostirório https://github.com/fga-eps-mds/2023.1-PyAnalyticsGit.git :

- O arquivo ‘.env’ deve estar assim para o exemplo acima:
  ```
  user_name = "fga-eps-mds"
  repo_name = "2023.1-PyAnalyticsGit"
  ```
### Relatório Estático
Gera relatórios de repositórios a partir da função “gerar_relatório” recebendo
como parâmetros os valores de usuários e/ou repositórios existentes do github:

- Exemplo: https://github.com/fga-eps-mds/2023.1-PyAnalyticsGit.git
- Utilize o método:
```
gerar_relatorio(’fga-eps-mds’,’2023.1-PyAnalyticsGit’)
```
- Lembre-se de mudar os parâmetros para o repositório em interesse.

Caso os parâmetros não sejam fornecidos, o relatório usará os valores das
variáveis de ambiente contidas em .env.
```
gerar_relatorio()
```

##
# 🤝 Colaboradores

| [<img src="https://github.com/gabrie1barbosa.png" width=80><br><sub>Gabriel Barbosa</sub>](https://github.com/gabrie1barbosa) |  [<img src="https://github.com/JeffersonSenaa.png" width=80><br><sub>Jefferson Sena</sub>](https://github.com/JeffersonSenaa) | [<img src="https://github.com/mateus9levy.png" width=80><br><sub>Mateus Levy</sub>](https://github.com/mateus9levy) |  [<img src="https://github.com/PedroHhenriq.png" width=80><br><sub>Pedro Henrique</sub>](https://github.com/PedroHhenriq) |  [<img src="https://github.com/rodfon3301.png" width=80><br><sub>Rodrigo Fonseca</sub>](https://github.com/rodfon3301) |   [<img src="https://github.com/Tiago1604.png" width=80><br><sub>Tiago Albuquerque</sub>](https://github.com/Tiago1604) |
| :---: | :---: | :---: |  :---: | :---: | :---: | 

##

## :ballot_box_with_check: Licença:
O PyAnalyticsGit é licenciado sob o MIT License. [licença](/LICENSE).
##



<div align=>
<img src="https://user-images.githubusercontent.com/98030427/236968066-315be92b-eabe-4d76-a5d7-bbaaa8df1e2d.png" width="200px" />
</div>
