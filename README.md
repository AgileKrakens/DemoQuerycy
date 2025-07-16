<img src="assets/demoquerycy_logo.png">

*Uma plataforma de civic tech para análise de dados parlamentares, construída com Flask e Python.*

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
---

## 1. Visão Geral do Projeto

O **DemoQuerycy** é uma aplicação web desenvolvida para combater a baixa fiscalização cidadã e a complexidade dos portais de transparência governamentais. A plataforma coleta, processa e apresenta dados sobre a atuação dos vereadores de São José dos Campos (mandato 2020-2024) de forma objetiva, visual e acessível, permitindo que qualquer cidadão possa compreender e analisar o desempenho de seus representantes.

**Problema:** Portais oficiais de dados políticos são, em geral, pouco intuitivos e de difícil navegação, criando uma barreira entre o cidadão e a informação.
**Solução:** Uma interface limpa e focada no usuário que resume e evidencia os dados mais relevantes da atividade parlamentar, como proposições, votações e frequência.

---

## 2. Arquitetura e Boas Práticas

Este projeto foi desenvolvido com foco em manutenibilidade, escalabilidade e segurança. As seguintes práticas e padrões de arquitetura foram implementados:

* **Estrutura Modular com Blueprints:** A aplicação utiliza **Blueprints** do Flask para organizar as funcionalidades em componentes desacoplados (ex: um blueprint para autenticação, outro para visualização de dados), facilitando a manutenção e a expansão do projeto.
* **Gerenciamento de Configuração e Segredos:** As credenciais do banco de dados e outras chaves sensíveis são gerenciadas através de **variáveis de ambiente** (utilizando arquivos `.env` e a biblioteca `python-dotenv`), evitando a exposição de dados sigilosos no código-fonte, conforme a metodologia *Twelve-Factor App*.
* **Processos de ETL para Coleta de Dados:** A coleta de dados foi estruturada como um processo de **ETL (Extract, Transform, Load)**. Scripts em Python realizam a extração (web scraping de portais HTML e consumo de APIs JSON governamentais), a transformação (limpeza e estruturação dos dados) e a carga (armazenamento no banco de dados).
* **Acesso Seguro ao Banco de Dados:** A comunicação com o banco de dados MySQL é feita utilizando um conector direto. Para prevenir vulnerabilidades, todas as consultas que envolvem dados de entrada são construídas utilizando **queries parametrizadas**, uma prática essencial de segurança para evitar ataques de SQL Injection.
* **Ambientes de Desenvolvimento Padronizados com Docker:** O projeto inclui uma configuração com **Docker e Docker Compose**, permitindo que qualquer desenvolvedor suba um ambiente de desenvolvimento idêntico e isolado com um único comando, garantindo consistência e eliminando problemas de configuração local.

---

## 3. Tecnologias Utilizadas

| Categoria          | Tecnologia                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| **Backend** | `Python 3.9+`, `Flask`                                                                                         |
| **Banco de Dados** | `MySQL`                                                                                                 |
| **Data Science** | `Pandas`, `Matplotlib`/`Seaborn` (para as análises estatísticas e geração de gráficos)                    |
| **Data Collection**| `Beautiful Soup 4`, `Requests`, `Selenium`                                                              |
| **DevOps** | `Docker`, `Docker Compose`                                                                                      |
| **Frontend** | `HTML5`, `CSS3`, `JavaScript`, `Bootstrap`                                                                    |

---

# MVP Demo - Sprint 3
## Demoquerycy v1.0
https://github.com/user-attachments/assets/5cf3eeb1-a711-4265-8404-cce7c57d41c7

# MVP Demo - Sprint 2
## Páginas: Perfil e Políticos
https://github.com/user-attachments/assets/b890285e-84ad-406f-a35d-badcc0d17ad9

## Data Scraping
https://github.com/user-attachments/assets/feadcc8b-f0f8-4840-99d5-b324d3745e62

# MVP Demo - Sprint 1
## Aplicação Web
https://github.com/user-attachments/assets/29591d73-230e-4df1-af40-73fbc30b7fe2

## crawler_personal_data
https://github.com/user-attachments/assets/09e7e4a4-59d7-4d1d-b844-55f1984ae509

# Descrição do MVP de cada Sprint

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
