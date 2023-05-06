## Requisitos

O objetivo desse documento é apresentar os requisitos funcionais e não funcionais do GitAnalisys, uma biblioteca em Python que gera relatórios automatizados em Markdown de
repositórios do GitHub.

## Requisitos Funcionais

**Interação com o Git**: A biblioteca deve ser capaz de interagir com o Git lendo os dados de saída dos comandos Git e criando o relatório a partir da interação
inicial com o repositório ou primeiro commit.

**Relatórios automatizados**: A biblioteca deve ser capaz de gerar relatórios automatizados atualizando os dados desse relatório a cada commit do projeto.

**Analise do desempenho do projeto**: A biblioteca deve ser capaz de analisar o desempenho do projeto podendo identificar problemas ou gargalos, tendências ao
longo do tempo, como crescimento ou a diminuição do número de commits, complexidade do cógido, etc... e uma análise detalhada de cada integrante, apresentando esses
dados no relatório.

**Geração do relatório em Markdown**: A biblioteca deve ser capaz de gerar relatórios automatizados no formato Markdown.

**Gráficos e tabelas**: A biblioteca deve ser capaz de gerar gráficos e tabelas nos releatórios que apresentem as informações e os dados de forma
clara e intuitiva.

## Requisitos Não Funcionais

**Segurança**: A biblioteca deve ser segura e garantir a privacidade dos dados do repositório.

**Acessibilidade**: A biblioteca deve ser fácil de instalar e usar, sem exigir configurações ou conhecimento avançado. Deve ser capaz de utilizar em diferentes sistemas
operacionais

**Eficiência**: A biblioteca deve ter um bom desempenho, gerando relatórios rapidamente. Os relatórios devem ser gerados em tempo hábil para que o desenvolvedor possa acompanhar as alterações sem atrasos ou interrupções significativas no fluxo de trabalho.

**Precisão**: A biblioteca deve ser confiável e ter baixo índice de erros e falhas.

**Volume**: A biblioteca deve ser capaz de lidar com grandes volumes de dados sem sobrecarregar e capaz de lidar com repositórios de grande porte.
