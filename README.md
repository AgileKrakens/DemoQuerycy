<img src="assets/demoquerycy_logo.png">

# Descrição:
O projeto nasceu em resposta à problemática da falta de engajamento político fora do período eleitoral e à falsa sensação de transparência no cenário democrático, onde muitos cidadãos confiam cegamente nas promessas feitas pelos candidatos durante essas campanhas. Nessa prerrogativa, buscamos evidenciar a atuação de cada político na câmara municipal de São José dos Campos.

Nesse contexto, é inevitável refletir sobre os modelos democráticos que moldaram nossa organização social. Na democracia ateniense, por exemplo, os cidadãos, ainda que representando apenas uma pequena parcela do corpo social, exerciam o poder de decisão política de forma direta, podendo influenciar no rumo das decisões políticas. Assim, eles defendiam seus interesses de maneira ativa no cenário político.

Entretanto, conforme as organizações políticas se expandiram para níveis nacionais, a prática da democracia direta tornou-se inviável. Reunir milhares de pessoas em uma praça para deliberar é impossível, e por isso elegemos representantes que, em teoria, defendem nossos interesses.

Portanto, diante da falta de engajamento político e dos desafios estruturais da democracia atual, desenvolvemos este software com o objetivo de, por meio do ambiente digital, reunir informações relevantes para que o eleitorado conheça melhor seus candidatos e suas ações no poder público. Dessa forma, podemos identificar quais políticos realmente defendem os interesses da população e são dignos de continuar como nossos representantes.

# Objetivo:
DemoQuerycy se propõe a ser uma alternativa digital para a participação efetiva e democrática dos cidadãos na conjuntura política. Nesse sentido, coletamos dados públicos referentes ao poder legislativo municipal. Utilizando scripts que coletam dados públicos referentes ao trabalho feito na camera dos vereados, também realizamos análises estatísticas do desempenho individual de cada vereador através desses dados. Dessa forma, considerando a complexidade dos documentos legais e a dificuldade de navegação no site oficial da câmara, nosso software busca trazer a devida transparência a essas informações e tornar a análise do desempenho do poder legislativo menos técnica, com o objetivo de ser acessível e conclusiva para qualquer público.

# Features - Sprint 1
## Aplicação Web

## crawler_personal_data


- Raspagem de dados pessoais de cada político
- Persistência dos dados em arquivos JSON

# Instalação e Utilização

```sh
git clone https://github.com/AgileKrakens/DemoQuerycy.git
```
```sh
cd /DemoQuerycy/src
```
```sh
python app.py
```

# Product Backlog

| Nº       | Requisitos Funcionais                                                                                           | Sprint | Prioridade |
|----------|-----------------------------------------------------------------------------------------------------|--------|------------|
| RF001.0  | O site precisa ter uma página com o perfil do vereador pesquisado.                                   | 1      | Alta       |
| RF001.1  | No perfil do candidato, é preciso uma seção que mostra a presença do vereador nas sessões.           | 2      | Média      |
| RF001.2  | No perfil do candidato, é preciso uma seção que mostra as proposições (Lei, Requerimento, Moção, Identificação) do vereador. | 2      | Média      |
| RF001.3  | No perfil do candidato, é preciso uma seção que mostra as leis aprovadas de autoria do vereador, e os temas em que ele mais atuou. | 2      | Média      |
| RF001.4  | No perfil do candidato, é preciso uma seção que mostra as comissões que o vereador participa, e os cargos dele em cada uma. | 2      | Baixa      |
| RF001.5  | No perfil do candidato, é preciso uma seção que mostra os seguintes dados do candidato: idade, formação, área profissional, histórico de mandatos em São José dos Campos e partidos em que atuou. | 1      | Média      |
| RF002.0  | O site deve ter uma página Home em que se pesquisa e é mostrado os candidatos e redireciona para a página do perfil. | 1      | Alta       |
| RF002.1  | A página Home precisa ter uma barra de pesquisa que permite ao usuário buscar algum vereador por nome. | 1      | Alta       |
| RF002.2  | A página Home precisa ter um mecanismo de filtragem que mostra os candidatos que pertencem ao partido selecionado. | 1      | Alta       |
| RF002.3  | A página Home deve possuir um índice com a lista do nome de todos os vereadores.                     | 1      | Alta       |
| RF003.0  | A página do perfil deve mostrar informações em relação ao tema das leis que o vereador mais aprovou.  | 3      | Alta       |
| RF003.1  | Um gráfico de barra com os 7 temas mais aprovados pelo vereador, mais outros "restantes" que podem ser ampliados e visualizadas as porcentagens. | 3      | Média      |
| RF003.2  | Uma janela de pesquisa por tema com listbox que mostra o output de quantos projetos aprovados o vereador tem naquele tema. | 3      | Alta       |
| RF003.3  | Ambos os gráficos devem ser acompanhados por um terceiro que é a média de todos os vereadores.       | 3      | Baixa      |
| RF004    | A página do perfil deve ter uma seção interativa que permite uma avaliação do candidato.             | 3      | Baixa      |

# Time

| Foto | Nome | Função | Github | Linkedin |
| :---------: | :---------: | :---------------------: | :-----------------: | :-------: |
| <img src="/assets/img_team/guiioshua.png" width=50px> | Guilherme Ioshua | Product Owner | <a href="https://github.com/guiioshua"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/guilherme-ioshua-sene/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/jodijotar.jpg" width=50px> | Fabio Fonseca | Scrum Master | <a href="https://github.com/jodijotar"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/fabiofonsecajodi/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/giovanni.jpg" width=50px> | Giovanni Kanjiscuk | Scrum Team | <a href="https://github.com/GKanjiscuk"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/giovanni-kanjiscuk/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/kawata.png" width=50px> | Matheus Kawata | Scrum Team | <a href="https://github.com/KwMajor"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/matheus-felipe-0832b52ba/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_marcos.png" width=50px> | Gabriel Marcos | Scrum Team | <a href="https://github.com/GabrieLMRDL"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/konishi.png" width=50px> | Vinícius Konishi |  Scrum Team  | <a href="https://github.com/Vinicius-Konishi"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_fernando.png" width=50px> | Gabriel Fernando |  Scrum Team  | <a href="https://github.com/Gabriel-Fernando-Lima"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="www.linkedin.com/in/gabriel-fernando-bb430b330"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| <img src="/assets/img_team/g_farias.png" width=50px> | Gabriel Farias |  Scrum Team  | <a href="https://github.com/FariasTheProgrammer"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |



