📘 Meta Python Developer Case

Projeto desenvolvido como demonstração prática para vaga de Desenvolvedor Python, focado em:

Integração com API REST

Tratamento e normalização de dados JSON

Persistência em PostgreSQL

Uso profissional de Docker e docker-compose

Boas práticas de organização, modularização e versionamento com Git

Este projeto simula um fluxo real de ETL leve usando Python + Requests + PostgreSQL em containers isolados.

🚀 Objetivo do Projeto

Criar um pipeline simples:

Consumir dados de uma API pública

Normalizar os campos necessários

Gravar/atualizar usuários em um banco PostgreSQL

Executar tudo em containers independentes (app + db)

Esse tipo de arquitetura é comum em:

microserviços Python

rotinas ETL

ingestão de dados

jobs de integração

pipelines Airflow

🏗️ Arquitetura do Sistema
flowchart LR
    API[API REST Pública] --> |JSON| APP[Container Python]
    APP --> |INSERT/UPDATE| DB[(PostgreSQL)]


app: código Python responsável por consumir API, transformar dados e inserir no banco.

db: instância PostgreSQL rodando em container dedicado.

Comunicação entre containers ocorre via rede interna Docker.

🧩 Tecnologias Utilizadas
Tecnologia	Uso
Python 3.12	processamento, normalização e gravação dos dados
Requests	consumo da API REST
PostgreSQL	armazenamento relacional
psycopg2-binary	driver Python para PostgreSQL
Docker	containerização
docker-compose	orquestração dos serviços
Git/GitHub	versionamento e portfólio
📁 Estrutura do Projeto
meta-python-developer-case/
├── app/
│   ├── __init__.py
│   ├── db.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


db.py → Conexão + criação de tabela + inserção/atualização

main.py → Orquestra a execução principal

Dockerfile → Ambiente Python configurado

docker-compose.yml → App + PostgreSQL + rede + volumes

⚙️ Instalação e Execução
1️⃣ Clonar o repositório
git clone https://github.com/SEUUSER/meta-python-developer-case.git
cd meta-python-developer-case

2️⃣ Subir os containers
docker-compose up --build


O Docker irá:

baixar a imagem do PostgreSQL

instalar dependências Python

iniciar ambos os containers

3️⃣ Ver logs do app
docker logs -f meta_app


Você verá:

conexão ao banco

criação da tabela

usuários sendo puxados da API

inserção com sucesso

🧪 Validar os Dados no Banco

Acessar o container do PostgreSQL:

docker exec -it meta_pg psql -U meta_user -d meta_db


Consultar a tabela:

SELECT * FROM api_users;


Você verá algo como:

id	name	username	email	city

Importados da API pública.

🧠 Explicação Técnica — Pontos Fortes do Projeto
✔️ Arquitetura limpa e modular

Código separado em camadas:

main.py → controle de fluxo

db.py → banco e queries

app folder → organiza o módulo

✔️ Uso correto de environment variables

Boa prática para apps escaláveis:

DB_HOST

DB_USER

API_URL

✔️ Tolerância a falhas

raise_for_status()

tratamento com try/finally

reconexão controlada

✔️ Docker configurado corretamente

app e db isolados

volumes persistentes

dependência entre serviços

Dockerfile leve (python:slim)

✔️ Repositório ideal para portfólio

Mostra domínio de:

Python profissional

API REST

SQL real

Docker

Modularização

Git/GitHub

Boas práticas

🔧 Possíveis Melhorias Futuras

Estas evoluções mostram maturidade técnica:

🔹 Criar uma API própria com FastAPI

Expor endpoints /users, /health, /stats.

🔹 Adicionar testes automatizados (pytest)
🔹 Criar pipeline CI com GitHub Actions

lint

testes

build docker

🔹 Adicionar Airflow

Rodar esse job diariamente como DAG.

🔹 Criar visualização de dados (Metabase / Grafana)
👨‍💻 Autor

Rafael dos Santos Vicente
Desenvolvedor Python | SQL | APIs | Docker
📧 Rafael.s_vicente@hotmail.com

🔗 GitHub: https://github.com/RafaelSV9

🔗 LinkedIn: https://www.linkedin.com/in/rafael-vicente998/
