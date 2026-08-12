# Guia de Arquitetura — BusList API

## Sumario
- [Introdução](#1-introdução)
- [Estrutura do Projeto](#2-estrutura-do-projeto)
- [Apps](#3-django-apps)
    - [User](#31-user)
    - [Bus](#32-bus)
    - [Student](#33-student)
    - [Trip](#34-trip)
    - [Attendance](#35-attendance)
- [Camada de Models](#4-camada-de-models)
- [Camada de Serializer](#5-camada-de-serializers)
- [Camada de View](#6-camada-de-views)
- [Service Layer](#7-service-layer)
- [Acesso aos Dados](#8-acesso-aos-dados--django-orm)
- [Tratamento de Exceções](#9-tratamento-de-exceções)
- [Autenticação e Segurança](#10-autenticação-e-segurança)
- [Docker](#11-docker)
- [Fluxo Completo de uma Requisição](#12-fluxo-completo-de-uma-requisição)
- [Princípios da Arquitetura](#14-princípios-da-arquitetura)

## 1. Introdução

A BusList API utiliza uma arquitetura organizada em camadas, com o objetivo de separar responsabilidades, facilitar a manutenção do código e permitir a evolução da aplicação.

A aplicação foi desenvolvida utilizando Django e Django REST Framework, com uma Service Layer responsável pela centralização das regras de negócio.

O fluxo principal de uma requisição pode ser representado da seguinte forma:

```Cliente -> URL -> View -> Serializer -> Service - > Django ORM -> PostgreSQL```


### 2 Estrutura do projeto

A aplicação é organizada utilizando Django Apps, onde cada App representa uma parte específica do domínio da aplicação.

```
Buslist-backend/
│
├── apps/
│ ├── user/
│ ├── bus/ 
│ ├── student/ 
│ ├── trip/ 
│ └── attendance/ 
│ 
├── core/ 
│ ├── exceptions/ 
│ ├── handlers/ 
│ └── error_messages/ 
│ 
├── config/ 
│ ├── settings.py 
│ ├── urls.py 
│ ├── asgi.py 
│ └── wsgi.py 
│ 
├── manage.py 
├── requirements.txt 
├── Dockerfile 
├── docker-compose.yml 
└── .env
```

A estrutura interna dos Apps pode variar conforme a implementação de cada módulo. O objetivo dessa organização é manter cada domínio isolado e facilitar a manutenção da aplicação.


## 3. Django Apps

A aplicação utiliza diferentes Django Apps para separar os principais domínios do sistema.

### 3.1 User

Responsável pelo gerenciamento dos usuários e pelos recursos relacionados à autenticação.

Principais responsabilidades:

- Cadastro de usuários;
- Autenticação;
- Geração de tokens JWT;
- Autenticação através de e-mail;
- Controle de usuários administradores.


### 3.2 Bus

Responsável pelo gerenciamento dos ônibus.

Principais responsabilidades:

- Cadastro de ônibus;
- Atualização;
- Consulta;
- Ativação e desativação;
- Validação da capacidade.

### 3.3 Student

Responsável pelo gerenciamento dos estudantes.

Principais responsabilidades:

- Cadastro;
- Atualização;
- Consulta;
- Remoção.

### 3.4 Trip

Responsável pelo gerenciamento das viagens.

Principais responsabilidades:

- Criação de viagens;
- Associação de ônibus;
- Associação de estudantes;
- Consulta das viagens.

### 3.5 Attendance

Responsável pelo controle de presença dos estudantes nas viagens.

Principais responsabilidades:

- Registro de presença;
- Associação entre estudante e viagem;
- Controle da participação dos estudantes.

## 4. Camada de Models

Os Models representam as entidades do domínio da aplicação.

Eles são utilizados pelo Django ORM para realizar o mapeamento entre os objetos Python e as tabelas do banco de dados.

As principais entidades são:

- User
- Bus
- Student
- Trip
- Attendance

Por exemplo, o Model Bus representa os dados de um ônibus e possui os campos necessários para armazená-los no banco.

O Django ORM permite realizar operações utilizando Python, sem a necessidade de escrever diretamente SQL para as operações mais comuns.

Exemplo:

```Bus.objects.filter(active=True)```

Essa operação representa uma consulta aos ônibus que estão ativos.


## 5. Camada de Serializers

Os Serializers fazem parte do Django REST Framework e são responsáveis principalmente por:

Validar dados recebidos pela API;
Converter dados recebidos em estruturas Python;
Converter objetos Python em dados JSON;
Preparar os dados que serão utilizados pela camada de serviço.

O fluxo de uma requisição pode ser representado como:

```JSON -> Serializer -> Vlaidação -> validate_data -> Service```


Por exemplo, ao criar um ônibus, os dados enviados pelo cliente passam primeiro pelo Serializer.

Depois da validação, os dados podem ser enviados para o Service responsável pela operação.

## 6. Camada de Views

As Views são responsáveis por receber e responder às requisições HTTP.

A View funciona como uma camada de entrada da aplicação.

Suas principais responsabilidades são:

- Receber a requisição;
- Identificar a operação solicitada;
- Utilizar o Serializer para validação;
- Chamar o Service responsável;
- Retornar a resposta HTTP.

As regras de negócio não devem ficar concentradas nas Views.

Exemplo conceitual:

```
POST /bus/

Request -> BusView -> BusSerializer -> BusService
```

## 7. Service Layer

A aplicação utiliza uma Service Layer para centralizar as regras de negócio.

Essa camada é responsável por executar operações que envolvem regras específicas do domínio.

Por exemplo, ao cadastrar um ônibus, o Service pode:

- Limpar os dados recebidos;
- Verificar se a placa já existe;
- Validar regras específicas;
- Criar o objeto;
- Persistir os dados através do Django ORM;
- Retornar o resultado da operação.

Exemplo:

```
BusService.create_bus() 
    │ 
    ├── Validações 
    │ 
    ├── Regras de negócio 
    │ 
    ▼
Bus.objects.create()
```

A utilização da Service Layer mantém as Views mais simples e permite concentrar as regras de negócio em locais específicos.

## 8. Acesso aos Dados — Django ORM

No projeto não existe uma camada Repository como no Spring Data JPA.

O acesso aos dados é realizado através do Django ORM, utilizando os Managers e QuerySets dos Models.

Exemplo:

```Bus.objects.filter(active=True)```

Ou:

```Bus.objects.get(id=bus_id)```

O Django transforma essas operações em consultas SQL que são executadas no PostgreSQL.

## 9. Tratamento de Exceções

A aplicação possui uma estrutura centralizada para tratamento de erros através da pasta core.

```
core/
├── exceptions/
├── handlers/
└── error_messages/
```

### Exceptions

Contém exceções personalizadas utilizadas pela aplicação.

Exemplos:

- UserNotFoundException
- EmailAlreadyExistsException
- InvalidCredentialsException

### Error Messages

Centraliza as mensagens de erro utilizadas pelas exceções.

Essa abordagem evita a duplicação de mensagens e facilita sua manutenção.

### Exception Handler

O projeto possui um handler personalizado responsável por integrar as exceções da aplicação ao mecanismo de tratamento de exceções do Django REST Framework.

Fluxo:

```Exception -> Custom Exception Handler -> HTTP Response```

## 10. Autenticação e Segurança

A autenticação da API utiliza JWT (JSON Web Token) através do Simple JWT.

O fluxo básico de autenticação é:

```
Login
  │
  ▼
Validação das credenciais
  │
  ▼
Geração do JWT
  │
  ├── Access Token
  │
  └── Refresh Token
```

Nas requisições protegidas, o cliente envia o Access Token no header:

```Authorization: Bearer <access_token>```

O Django REST Framework utiliza a classe de autenticação JWT configurada no projeto para validar o token antes de permitir o acesso ao endpoint.

## 11. Docker

O projeto utiliza Docker para criar um ambiente padronizado de execução.

O ```docker-compose.yml``` define os serviços utilizados pela aplicação.

O Docker Compose permite que os containers sejam executados e conectados através de uma mesma rede.

Dentro da rede Docker, o Django pode acessar o PostgreSQL utilizando o nome do serviço definido no Compose, como:

```db```

Já aplicações externas, como DBeaver ou pgAdmin, acessam o PostgreSQL através da porta publicada no computador host.

## 12. Fluxo Completo de uma Requisição

Considerando uma requisição para criação de um ônibus:

```
Cliente
    │ 
    │ POST /bus/
    ▼
URL
    │
    ▼
BusView
    │
    ▼
BusSerializer
    │
    │ Valida dados
    ▼
BusService
    │
    │ Regras de negócio
    ▼
Django ORM
    │
    │ SQL
    ▼
PostgreSQL
    │
    │ Resultado
    ▼
Django ORM
    │
    ▼
Service
    │
    ▼
Serializer
    │
    ▼
HTTP Response
    │
    ▼
Cliente
```

Esse fluxo permite manter cada componente responsável por uma parte específica do processamento da requisição.

## 14. Princípios da Arquitetura

A organização da aplicação busca seguir os seguintes princípios:

- Separação de responsabilidades;
- Baixo acoplamento entre componentes;
- Centralização das regras de negócio;
- Reutilização de código;
- Facilidade de manutenção;
- Organização por domínio;
- Separação entre entrada de dados, regras de negócio e persistência.

A arquitetura foi construída buscando aplicar conceitos utilizados em projetos profissionais de backend, adaptando-os ao ecossistema Django.