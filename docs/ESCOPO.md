# Escopo do projeto
Este documento de escopo tem como objetivo definir o escopo do projeto da biblioteca PyAnalyticsGit para geração de relatórios automatizados a partir de repositórios do GitHub. O documento descreve os épicos, features e histórias do usuários, além das restrições do projeto.

## Requisitos

Os requisitos exigidos para o desenvolvimento do projeto estão em [Requisitos](https://github.com/fga-eps-mds/2023.1-Biblioteca-Relatorios-Git/blob/main/docs/REQUISITOS.MD)

## Objetivos do produto/projeto

**Público alvo**

Essa biblioteca é destinada aos  gestores e líderes de equipes de desenvolvimento que trabalham com repositórios Git e desejam gerar relatórios textuais, estatísticos e gráficos a partir do histórico de commits do projeto.
Desenvolvedores e equipes que desejam acompanhar o desempenho do projeto e identificar possíveis problemas ou oportunidades de melhoria também podem utilizar a biblioteca com proveito.

**Restrições e Limitações**

- A biblioteca dependerá de acesso à internet para se conectar à API do GitHub e extrair os dados necessários.
- A biblioteca estará sujeita às limitações e políticas de uso da API do GitHub, incluindo limites de taxa (rate limits) e restrições de acesso.
- O escopo do projeto se limita à extração de dados de commits, issues e milestones. Outras funcionalidades do GitHub, como pull requests, não serão contempladas neste projeto.

**Épicos**

+ A biblioteca deve ser capaz de interagir com o Git. 
+ A biblioteca deve ser capaz de analisar o desempenho do projeto e extrair dados do repositório.  
+ A biblioteca deve ser capaz de gerar relatórios automatizado.

**Features**

+ A biblioteca deve ser capaz de ler os dados de saída  dos comandos Git
+ A biblioteca deve ser capaz de extrair dados de Commits, issues e milestones de um repositório
+ A biblioteca deve ser capaz de interagir com o repositório escolhido pelo usuário;
+ A biblioteca deve conter tabelas que apresentem os dados do repositório no relatório
+ A biblioteca deve conter elementos textuais do repositório a partir da geração de uma Nuvem de Palavras
+ A biblioteca deve ser capaz de gerar gráficos visuais e adiciona-los ao relatório
+ A biblioteca deve atualizar automaticamente os dados do relatório a cada commit
+ A biblioteca deve gerar o relatório em formato Markdown
+ A biblioteca deve estar no PyPl e disponível para instalação por meio do pip.  


**Histórias de usuário**


| História de Usuário | Critérios de Aceitação |
|---------------------|------------------------|
| Eu como um usuário quero que a  biblioteca gere relatórios para que possa analisar o andamento e desempenho do meu projeto  | 1. Não pode gerar relatórios vazios.  |
| Eu como um usuário quero que a  biblioteca seja capaz de analisar o desempenho do projeto para que eu posso identificar possíveis problemas  | 1. Os dados de desempenho ao longo do tempo do usuário não devem ser corrompidos 2. A biblioteca deve ser capaz de identificar a quantidade de issues abertas e fechadas por período para avaliar a eficiência do processo de resolução de problemas |
| Eu como um usuário quero que a biblioteca extraia os dados dos commits de um repositório, incluindo autor, data e mensagem associada.  | 1. Os dados dos commits devem ser extraídos corretamente da API do GitHub. 2. As informações de autor, mensagem e data devem ser obtidas para cada commit. |
| Eu como um usuário, desejo extrair os dados das issues de um repositório, incluindo título, número, estado e labels associadas.  | 1. Os dados das issues devem ser extraídos corretamente da API do GitHub. 2. Como um usuário, desejo extrair os dados das issues de um repositório, incluindo título, número, estado e labels associadas. |
| Eu como um usuário quero que a biblioteca extraia os dados os dados das milestones de um repositório, incluindo título, número de issues e issues relacionadas.  | 1. os dados das milestones de um repositório, incluindo título e número de issues relacionadas. 2. os dados das milestones de um repositório, incluindo título, issues e número de issues relacionadas. |
| Eu como um usuário, desejo que a biblioteca gere tabelas formatadas em Markdown com as informações extraídas dos commits, issues e milestones.  | 1. As tabelas geradas devem seguir a formatação correta do Markdown. 2. As informações dos commits, issues e milestones devem ser apresentadas de forma organizada e legível nas tabelas.  |
| Eu como um usuário, desejo que a biblioteca gere gráficos visuais para representar métricas e estatísticas relevantes do projeto.  | 1. Os gráficos gerados devem ser claros e informativos. 2. As métricas e estatísticas apresentadas nos gráficos devem ser baseadas nos dados extraídos dos commits, issues e milestones.  |
| Eu como um usuário quero que a  biblioteca gere relatórios em Markdown para que o relatórios esteja no próprio GitHub.  | 1. A biblioteca deve ser capaz de gerar relatórios em formato Markdown a partir dos dados analisados do repositório Git 2. O arquivo Markdown gerado pode conter gráficos e tabelas com as métricas analisadas  |
| Eu como um usuário quero que a biblioteca gera relatórios automatizados a cada commit  para que eu possa acompanhar as alterações de forma organizada. | 1. Os relatórios gerados devem ser salvos em um local de fácil acesso para o time de desenvolvimento, como o github 2. A biblioteca deve ser fácil de usar e configurar pelo desenvolvedor, com documentação clara organizada |  


