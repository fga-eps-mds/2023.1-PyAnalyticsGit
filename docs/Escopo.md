# Escopo do projeto

## Requisitos

Os requisitos exigidos para o desenvolvimento do projeto estão em [Requisitos](https://github.com/fga-eps-mds/2023.1-Biblioteca-Relatorios-Git/blob/main/docs/REQUISITOS.MD)

## Objetivos do produto/projeto

**Público alvo**

Essa biblioteca é destinada aos  desenvolvedores e equipes de desenvolvimento que trabalham com repositórios Git e desejam gerar relatórios textuais, estatísticos e gráficos a partir do histórico de commits do projeto.
Especificamente, desenvolvedores que desejam acompanhar o desempenho do projeto e identificar possíveis problemas ou oportunidades de melhoria

**Épicos**

+ A biblioteca deve ser capaz de interagir com o Git. 
+ A biblioteca deve ser capaz de analisar o desempenho do projeto.  
+ A biblioteca deve ser capaz de gerar relatórios automatizados 
+ O relatório deve conter informações detalhadas do repositório  

**Features**

+ A biblioteca deve ser capaz de ler os dados de saída  dos comandos Git 
+ A biblioteca deve ser capaz de identificar problemas ou gargalos no desempenho e apresenta-los no relatório.
+ A biblioteca deve atualizar automaticamente os dados do relatório a cada commit
+ Os relatórios devem conter gráficos que apresentem as informações de forma clara e intuitiva.
+ Os métodos da biblioteca devem ser iniciados a partir do commit  
+ A biblioteca deve ser capaz de mostrar uma análise detalhada de cada integrante do projeto
+ A biblioteca deve gerar ao relatório em formato Markdown
+ O relatório deve conter tabelas que apresentem os dados do repositório 
+ A biblioteca deve criar o relatório a partir da interação inicial com o repositório ou primeiro commit  
+ A biblioteca deve ser capaz de identificar as tendências conforme o tempo, como o crescimento ou a diminuição de número de Commits, complexidade do código, etc..
+ A biblioteca deve estar no PyPl e disponível para instalação por meio do pip.  
+ O relatório deve conter elementos textuais do repositório  
+ Os dados do repositorio possuem um número limitado sendo eles as alterações mais recentes do repositório 


**Histórias de usuário**


| História de Usuário | Critérios de Aceitação |
|---------------------|------------------------|
| Eu como desenvolvedor quero que a  biblioteca que gere relatórios para que posso analisar o andamento e desempenho do meu projeto  | 1. Não pode gerar relatórios vazios 2. A biblioteca, caso identifique que não houve progresso, não vai carregar o relatório.  |
| Eu como desenvolvedor quero relatórios com gráficos e tabelas para que possa ver e compreender dados de forma mais clara. | 1. Os gráficos e tabelas gerados devem ser claros e fáceis para que o desenvolvedor possa entender, com legendas e cores bem definidas para facilitar a interpretação dos dados e possíveis erros | 
| Eu como desenvolvedor quero que a  biblioteca seja capaz de analisar o desempenho do projeto para que eu posso identificar possíveis problemas  | 1. Os dados de desempenho ao longo do tempo do usuário não devem ser corrompidos 2. A biblioteca deve ser capaz de identificar a quantidade de issues abertas e fechadas por período para avaliar a eficiência do processo de resolução de problemas |
| Eu como desenvolvedor quero que a  biblioteca gere relatórios em Markdown para que o relatórios esteja no próprio GitHub.  | 1. A biblioteca deve ser capaz de gerar relatórios em formato Markdown a partir dos dados analisados do repositório Git 2. O arquivo Markdown gerado pode conter gráficos e tabelas com as métricas analisadas  |
| Eu como desenvolvedor quero que a biblioteca gera relatórios automatizados a cada commit  para que eu possa acompanhar as alterações de forma organizada. | 1. Os relatórios gerados devem ser salvos em um local de fácil acesso para o time de desenvolvimento, como o github 2. A biblioteca deve ser fácil de usar e configurar pelo desenvolvedor, com documentação clara organizada |  


