<img src="assets/demoquerycy_logo.png">

# Descrição:
O projeto nasceu em resposta à problemática da falta de engajamento político fora do período eleitoral e à falsa sensação de transparência no cenário democrático, onde muitos cidadãos confiam cegamente nas promessas feitas pelos candidatos durante essas campanhas. Nessa prerrogativa, buscamos evidenciar a atuação de cada político na câmara municipal de São José dos Campos.

Nesse contexto, é inevitável refletir sobre os modelos democráticos que moldaram nossa organização social. Na democracia ateniense, por exemplo, os cidadãos, ainda que representando apenas uma pequena parcela do corpo social, exerciam o poder de decisão política de forma direta. Assim, eles defendiam seus interesses de maneira ativa no cenário político.

Entretanto, conforme as organizações políticas se expandiram para níveis nacionais, a prática da democracia direta tornou-se inviável. Reunir milhares de pessoas em uma praça para deliberar é impossível, e por isso elegemos representantes que, em teoria, defendem nossos interesses.

Portanto, diante da falta de engajamento político e dos desafios estruturais da democracia atual, é notório de que apenas um povo informado é capaz de realizar o exercício da democracia, e desse modo, terceirizar a defesa de seus direitos e reivindicações através de um representante. Pensando nisso, desenvolvemos este software com o objetivo de, por meio do ambiente digital, reunir informações relevantes para que o eleitorado conheça melhor seus candidatos e suas ações no poder público. Dessa forma, podemos identificar quais políticos realmente defendem os interesses da população. 

# Objetivo:
DemoQuerycy se propõe a ser uma alternativa digital para a participação efetiva e democrática dos cidadãos na conjuntura política. Nesse sentido, coletamos dados públicos referentes ao poder legislativo municipal. 

Utilizando scripts que coletam dados públicos referentes ao trabalho feito na camera dos vereadores, também realizamos análises estatísticas do desempenho individual de cada vereador através desses dados.

Dessa forma, considerando a complexidade dos documentos legais e a dificuldade de navegação no site oficial da câmara, nosso software busca trazer a devida transparência a essas informações e tornar a análise do desempenho do poder legislativo menos técnica, com o objetivo de ser acessível e conclusiva para qualquer público.
# Features - Sprint 3
## Demoquerycy v1.0
https://github.com/user-attachments/assets/5cf3eeb1-a711-4265-8404-cce7c57d41c7

## Persistência de dados
- Devops e configuração do ambiente do projeto em um servidor local com objetivo de reunir e encapsular as dependencias do projeto
## Analise de dados
- geração de gráficos por autor que relatam a quantidade de projetos de leis aprovados, considerando os temas como parâmetro de análise
## UX
- Remodelação da estilização das páginas

# Features - Sprint 2
## Páginas: Perfil e Políticos
https://github.com/user-attachments/assets/b890285e-84ad-406f-a35d-badcc0d17ad9

- Página Políticos:
  * Geração automatizada dos Cards
  * Barra de pesquisa: filtragem dos cards por nome do político correspondente
- Página Perfil
  * Inserção de novas informações biográficas e dados relevantes sobre a atuação do político na câmara
  * Estilização da página
## Data Scraping
https://github.com/user-attachments/assets/feadcc8b-f0f8-4840-99d5-b324d3745e62

- crawler_personal_data:
  * Implementação de novos módulos: Área profissional, Comissões, Histórico de mandatos e Presença/Falta de cada político nas sessões
  * Salvamento dos JSON com base no Endpoint da aplicação: exibição dos dados automatizada e sincronização com outros componentes

# Features - Sprint 1
## Aplicação Web
https://github.com/user-attachments/assets/29591d73-230e-4df1-af40-73fbc30b7fe2

- Página Home:
  * Barra de pesquisa
  * Carrosel
- Escalabilidade da Página Perfil:
  * Dados biográficos 
  * Estrutura geral
## crawler_personal_data
https://github.com/user-attachments/assets/09e7e4a4-59d7-4d1d-b844-55f1984ae509

- Raspagem de dados pessoais de cada político
- Persistência dos dados em arquivos JSON

# MVP de Cada Sprint

## Sprint 1

### Páginas
- **Páginas com HTML prototípico**
  - Página Home
  - Página de Perfis
- **Wireframes**
  - Features estáticas do site
  - Features dinâmicas para dados individualizados dos políticos

### Dados Biográficos
- **Coleta de Dados**
  - Início da automatização da coleta de dados biográficos (Webcrawler)
  - Criação automatizada do perfil dos políticos cadastrados
  - Inserção automática dos primeiros dados no perfil de maneira escalável (Flask)

### Implementação da Aplicação
- **Servidor Funcional**
  - Página Home com carrossel e barra de pesquisa funcional
  - Perfis de políticos com estruturação de informações biográficas básicas

## Sprint 2

### Página 'Políticos'
- **Cards dos Políticos**
  - Foto, nome e partido de todos os políticos registrados
  - Redirecionamento para o perfil do político selecionado
- **Sistema de Pesquisa**
  - Pesquisa simples por nome do político

### Término dos Dados Biográficos
- **Coleta de Dados**
  - Finalização da coleta de dados biográficos (Webcrawler)
  - Display automatizado de todas as informações

### Coleta e Implementação dos Dados dos Mandatos
- **Informações sobre Presença**
  - Seção com informações de presença nas sessões plenárias
  - Comparação com a média da câmara
- **Comissões**
  - Listagem das comissões das quais o político participa
- **Histórico de Mandatos**
  - Histórico de mandatos e partidos anteriores

## Sprint 3

### Coleta e Armazenamento de Proposições
- **Proposições dos Políticos**
  - Coleta automatizada das proposições (crawler)
  - Estruturação em tabelas (MySQL) com:
    - Autor
    - Data
    - Tipo (ação, moção, indicação ou lei)
    - Tema
    - Status

### Implementação das Informações nos Perfis
- **Tabelas Interativas**
  - Proposições não legislativas (ações, moções e indicações)
  - Leis aprovadas pelo político

### Gráficos de Temas de Lei
- **Seções de Gráficos**
  - Gráfico fixo com ~7 temas mais aprovados pelo vereador
  - Gráfico interativo:
    - Pesquisa e seleção de um tema
    - Número absoluto de leis aprovadas nesse tema
    - Composição relativa (porcentagem) do tema na atuação legislativa

---

# Product Backlog

## Requisitos Funcionais do projeto

| Nº do Requisito | Requisitos | Sprint | Prioridade |
| --- | --- | --- | --- |
| RF001.0 | O site precisa ter uma página com o perfil do vereador pesquisado. | 1 | Alta |
| RF002.0 | O site deve ter uma página Home de onde se redireciona aos perfis dos candidatos | 1 | Alta |
| RF002.1 | A página home precisa ter uma rápida introdução ao projeto | 1 | Alta |
| RF002.2 | A página home precisa ter um carrossel com cards clicáveis que redirecionam para o página do perfil do político | 1 | Alta |
| RF002.3 | A página home precisa ter um botão de redirecionamento para a página “Políticos” | 1 | Alta |
| RF002.4 | A página “Políticos” deve ter listados todos os cards com nome, foto e partido dos políticos e uma barra de pesquisa por nome. | 2 | Alta |
| RF001.1 | No perfil do candidato, é preciso uma seção que mostra a presença do vereador nas sessões | 2 | Média |
| RF001.5 | No perfil do candidato, é preciso uma seção que mostra os seguintes dados do candidato: nome, partido, telefone, idade, formação, área profissional, histórico de mandatos em São José dos Campos e partidos em que atuou.  | 2 | Média |
| RF001.4 | No perfil do candidato, é preciso uma seção que mostra as comissões que o vereador participa, e os cargos dele em cada uma | 2 | Baixo |
| RF003.0 | A página do perfil deve mostrar informações em relação ao tema das leis que o vereador mais aprovou  | 3 | Alta |
| RF003.1 | Um gráfico de barra com os 7 temas mais aprovados pelo vereador, mais outros “restantes” | 3 | Média |

| Requisito | Cartão | Sprint |
| --- | --- | --- |
| RF001.0 | Eu, como eleitor, gostaria de visualizar as informações pessoais e estatísticas de um vereador em uma página dedicada para seu perfil. | 1 |
| RF002.0 | Eu, como eleitor, gostaria de ter uma página de recepção do site em que eu possa a partir dela acessar os perfis individuais. | 1 |
| RF002.1 | Eu, como eleitor, gostaria de pesquisar o nome do vereador em uma barra de pesquisa, assim ter acesso ao perfil de vereadores com este nome. | 1 |
| RF001.1 | Eu, como eleitor, gostaria de uma seção na página do perfil de cada político que mostra os dados da presença e faltas nas sessões do vereador. | 2 |
| RF001.4 | Eu, como eleitor, gostaria de uma seção com informações sobre as comissões em que o vereador participa e as funções em que ele atuou na página de seu perfil. | 2 |
| RF001.5 | Eu, como eleitor, gostaria de ver uma “seção” lateral com dados biográficos e histórico profissional do vereador na página do perfil. | 2 |
| RF002.3 | Eu, como eleitor, gostaria de visualizar uma página “Políticos” que possui cards com foto, nome e partido de todos os políticos registrados, para que eu seja redirecionado para o perfil do político ao clicar no card. | 2 |
| RF002.4 | Eu, como eleitor, gostaria de uma barra de pesquisa na página “Políticos” que filtra os cards correspondentes ao nome que eu pesquisei. | 2 |
| RF001.3 | Eu, como eleitor, gostaria de ter uma tabela mostrando todas as leis aprovadas pelo político em São José dos Campos. | 3 |
| RF001.2 | Eu, como eleitor, gostaria de ter uma tabela mostrando todas as proposiçãoes apresentadas pelo político em São José dos Campos. | 3 |
| RF003.0 e RF003.1 | Eu, como usuário, gostaria de uma seção do perfil com um gráfico de barras que mostra os temas em que o político mais aprovou leis. | 3 |

# Time

| Foto | Nome | Função | Github | Linkedin |
| :---------: | :---------: | :---------------------: | :-----------------: | :-------: |
| <img src="/assets/img_team/guiioshua.png" width=50px> | Guilherme Ioshua | Product Owner | <a href="https://github.com/guiioshua"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/guilherme-ioshua-sene/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/jodijotar.jpg" width=50px> | Fabio Fonseca | Scrum Master | <a href="https://github.com/jodijotar"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/fabiofonsecajodi/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/giovanni.jpg" width=50px> | Giovanni Kanjiscuk | Scrum Team | <a href="https://github.com/GKanjiscuk"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/giovanni-kanjiscuk/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/kawata.png" width=50px> | Matheus Felipe | Scrum Team | <a href="https://github.com/KwMajor"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/matheus-felipe-0832b52ba/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_marcos.png" width=50px> | Gabriel Marcos | Scrum Team | <a href="https://github.com/GabrieLMRDL"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/konishi.png" width=50px> | Vinícius Konishi |  Scrum Team  | <a href="https://github.com/Vinicius-Konishi"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/vin%C3%ADcius-greg%C3%B3rio-406640232?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_fernando.png" width=50px> | Gabriel Fernando |  Scrum Team  | <a href="https://github.com/Gabriel-Fernando-Lima"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="www.linkedin.com/in/gabriel-fernando-bb430b330"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_farias.png" width=50px> | Gabriel Farias |  Scrum Team  | <a href="https://github.com/FariasTheProgrammer"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="www.linkedin.com/in/gabrielrodfarias"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
