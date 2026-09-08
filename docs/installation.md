# Guia de Instalação — BusList API

Este documento apresenta o passo a passo para configurar e executar a BusList API utilizando Docker.

O objetivo é permitir que a aplicação seja executada em um ambiente local sem a necessidade de instalar manualmente o Python, PostgreSQL ou as dependências do projeto.

Toda a aplicação será executada através de containers Docker.


## Sumario
- [Pré-requisitos](#1-pré-requisitos)
    - [Docker](#11-docker-desktop)
    - [Git](#12-git)
    - [DBeaver](#13-dbeaver)
    - [Postman](#32-bus)
- [Clonando Projeto](#2-clonando-o-projeto)
- [Estrutura do Projeto](#3-estrutura-do-projeto)
- [Configuração do Ambiente](#4-configuração-do-ambiente-env)
- [Configuração do Banco no Django](#5-configuração-do-banco-no-django)
- [Construindo e Executando a Aplicação](#6-construindo-e-executando-a-aplicação)
- [Verificando os Containers](#7-verificando-os-containers)
- [Executando as Migrations](#8-executando-as-migrations)
- [Criando um Usuário Administrador](#9-criando-um-usuário-administrador)
- [Acessando a Aplicação](#10-acessando-a-aplicação)
- [Documentação da API](#11-documentação-da-api)
- [Testando a API](#12-testando-a-api)
- [Acessando o Banco de Dados pelo DBeaver](#13-acessando-o-banco-de-dados-pelo-dbeaver)
- [Comandos úteis do Docker](#14-comandos-úteis-do-docker)
- [Problemas Comuns](#15-problemas-comuns)
    - [Erro: failed to resolve host 'db'](#151-erro-failed-to-resolve-host-db)
    - [Erro: porta 5432 já está sendo utilizada](#152-erro-porta-5432-já-está-sendo-utilizada)
    - [Erro de incompatibilidade entre PostgreSQL 16 e 17](#153-erro-de-incompatibilidade-entre-postgresql-16-e-17)
    - [Containers não iniciam](#154-containers-não-iniciam)
    - [A API não responde](#155-a-api-não-responde)
- [Conclusão](#17-conclusão)
    

## 1. Pré-requisitos

Antes de iniciar, certifique-se de que os seguintes programas estejam instalados:

- Python 3.13
- Git
- PostgreSQL 17
- DBeaver ou pgAdmin (opcional, para gerenciamento visual do banco)
- Docker

### 1.1 Docker Desktop

O Docker Desktop é responsável por executar os containers da aplicação.

Download:

https://www.docker.com/products/docker-desktop/

Para verificar se o Docker está instalado:

```docker --version```

Para verificar o Docker Compose:

```docker compose version```

### 1.2 Git

O Git será utilizado para clonar o projeto.

Download:

https://git-scm.com/downloads

Para verificar:

```git --version```

### 1.3 DBeaver

O DBeaver é opcional e pode ser utilizado para visualizar e consultar o banco de dados PostgreSQL.

Download:

https://dbeaver.io/download/

### 1.4 Postman

O Postman é opcional e pode ser utilizado para testar os endpoints da API.

Download:

https://www.postman.com/downloads/


## 2. Clonando o projeto

Primeiro, clone o repositório do projeto:

```git clone https://github.com/Thiago-sys2/Buslist-backend-django```

Entre na pasta do projeto:

```cd Buslist-backend-backend```

## 3. Estrutura do projeto

A estrutura inicial será semelhante a:

```
Buslist-backend/
├── apps/
├── config/
├── core/
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── .env
```


## 4. Configuração do ambiente (.env)

Crie um arquivo chamado:

```.env```

na raiz do projeto.

Adicione as seguintes configurações:

```
POSTGRES_DB=buslist
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres123
POSTGRES_HOST=db
POSTGRES_PORT=5432
```


## 5. Configuração do banco no Django

No arquivo:

```config/settings.py```

a configuração do banco deve utilizar as variáveis de ambiente:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    }
}
```

Dessa forma, as informações de conexão não precisam ficar diretamente escritas no código.

## 6. Construindo e executando a aplicação

Na raiz do projeto, execute:

```docker compose up --build```

O Docker Compose irá:

- Construir a imagem do Django;
- Baixar a imagem do PostgreSQL;
- Criar os containers;
- Criar a rede entre os serviços;
- Iniciar o PostgreSQL;
- Iniciar o Django.

A estrutura será semelhante a:

```
Docker Compose
│
├── buslist-django
│   └── Django API
│
└── buslist-django-postgres
    └── PostgreSQL
```


## 7. Verificando os containers

Abra outro terminal e execute:

```docker ps```

Os containers deverão estar em execução.

Exemplo:

```
buslist-django
buslist-django-postgres
```

Também é possível visualizar todos os containers:

```docker ps -a```


## 8. Executando as migrations

As migrations são responsáveis por criar e atualizar a estrutura das As migrations são responsáveis por criar e atualizar a estrutura das tabelas do banco de dados de acordo com os models do Django.

Com os containers da aplicação em execução, execute o comando abaixo:

```docker exec -it buslist-django python manage.py migrate```

Após a execução, o Django aplicará todas as migrations pendentes no banco de dados.

Para verificar o estado das migrations:

```docker exec -it buslist-django python manage.py showmigrations```

As migrations aplicadas serão indicadas por:

```[X]```

Exemplo:

bus
```[X] 0001_initial```

student
```[X] 0001_initial```

trip
```[X] 0001_initial```


## 9. Criando um usuário administrador

O projeto possui um comando personalizado para transformar um usuário existente em administrador.

Primeiro, certifique-se de que o usuário já esteja cadastrado.

Dentro do container Django:

```python manage.py make_admin email_do_usuario```

Exemplo:

```python manage.py make_admin admin2@gmail.com```

Também é possível executar diretamente pelo terminal do computador:

```docker exec -it buslist-django python manage.py make_admin admin2@gmail.com```


## 10. Acessando a aplicação

Após os containers serem iniciados, a API estará disponível em:

http://localhost:8000


## 11. Documentação da API

A aplicação utiliza Swagger/OpenAPI para documentação dos endpoints.

Acesse:

http://localhost:8000/api/docs/

O caminho exato depende da configuração existente no arquivo config/urls.py.

A documentação permite visualizar e testar os endpoints da API.

## 12. Testando a API

A API pode ser testada utilizando o Postman ou Swagger.

O fluxo básico de utilização é:

1. Criar usuário
2. Fazer login
3. Receber JWT
4. Enviar JWT nas requisições protegidas
5. Criar e consultar recursos da API

Para endpoints protegidos, utilize:

```Authorization: Bearer <TOKEN>```

## 13. Acessando o banco de dados pelo DBeaver

O PostgreSQL está sendo executado dentro de um container Docker.

Para acessá-lo através do computador, ```o docker-compose.yml``` deve realizar o mapeamento da porta.

Exemplo:

ports:
  - ```5433:5432```

Isso significa:

```
Computador                    Docker
localhost:5433  ────────────> PostgreSQL:5432
```

Portanto, no DBeaver:

```
Host: localhost
Port: 5433
Database: buslist
User: postgres
Password: postgres123
```

Importante: a porta 5433 é a porta utilizada pelo computador para acessar o PostgreSQL. Dentro da rede Docker, o PostgreSQL continua utilizando a porta 5432.

Depois de conectar, será possível visualizar as tabelas criadas pelo Django.

Exemplo:

```
bus
student
trip
attendance
user
```

Também será possível verificar os registros criados através das requisições realizadas no Postman.

## 14. Comandos úteis do Docker

### 14.1 Subir a aplicação
```docker compose up```

### 14.2 Subir reconstruindo as imagens
```docker compose up --build```

### 14.3 Executar em segundo plano
```docker compose up -d```

### 14.4 Parar os containers
```docker compose stop```

### 14.5 Parar e remover os containers
```docker compose down```

### 14.6 Ver containers em execução
```docker ps```

### 14.7 Ver todos os containers
```docker ps -a```

### 14.8 Visualizar logs do Django
```docker logs -f buslist-django```

### 14.9 Visualizar logs do PostgreSQL
```docker logs -f buslist-postgres```

### 14.10 Acessar o container Django
```docker exec -it buslist-django bash```

### 14.11 Executar migrations
```docker exec -it buslist-django python manage.py migrate```

### 14.12 Criar migrations

Caso algum model seja alterado:

```docker exec -it buslist-django python manage.py makemigrations```

Depois:

```docker exec -it buslist-django python manage.py migrate```

### 14.13 Verificar migrations
```docker exec -it buslist-django python manage.py showmigrations```

## 15. Problemas comuns

### 15.1 Erro: failed to resolve host 'db'

Caso apareça:

```failed to resolve host 'db'```

isso normalmente significa que o Django está tentando acessar o banco através do hostname ```db``` fora da rede Docker.

Por exemplo, executar diretamente no Windows:

```python manage.py runserver```

não é recomendado neste ambiente.

A aplicação deve ser executada através do Docker:

```docker compose up```

O hostname:

```db```

é resolvido dentro da rede criada pelo Docker Compose.

### 15.2 Erro: porta 5432 já está sendo utilizada

Caso a porta ```5432``` já esteja sendo utilizada por uma instalação local do PostgreSQL, utilize outra porta no computador.

Por exemplo:

ports:
  - ```5433:5432```

Nesse cenário:

### Django → PostgreSQL
```db:5432```

### DBeaver → PostgreSQL
```localhost:5433```

Essas configurações são diferentes porque representam redes diferentes.

### 15.3 Erro de incompatibilidade entre PostgreSQL 16 e 17

Caso apareça:

```database files are incompatible with server```

e uma mensagem indicando que o diretório foi inicializado pelo PostgreSQL 16 enquanto o container utiliza PostgreSQL 17, existe um volume antigo criado por outra versão do PostgreSQL.

Em um ambiente de desenvolvimento onde os dados podem ser descartados, pode ser necessário remover os volumes:

```docker compose down -v```

Depois:

```docker compose up --build```

Atenção: o comando ```docker compose down -v remove``` os volumes associados ao projeto e pode apagar os dados do banco.

### 15.4 Containers não iniciam

Verifique:

```docker ps -a```

Depois consulte os logs:

```docker logs buslist-django```

e:

```docker logs buslist-postgres```

### 15.5 A API não responde

Verifique se o container Django está em execução:

```docker ps```

Também verifique os logs:

```docker logs -f buslist-django```

A API deverá estar disponível em:

http://localhost:8000

## 17. Conclusão

Após seguir este guia, o projeto estará configurado para funcionar utilizando Docker.

Não será necessário instalar manualmente:

```
Python;
PostgreSQL;
Dependências Python;
Ambiente virtual (venv).
```

O Docker será responsável por fornecer o ambiente necessário para executar a aplicação.

Para iniciar o projeto:

```docker compose up --build```

Após a inicialização:

API:
http://localhost:8000

```
Banco:
localhost:5433
```

```
Database:
buslist
```

O Postman poderá ser utilizado para testar a API e o DBeaver para visualizar os dados armazenados no PostgreSQL.