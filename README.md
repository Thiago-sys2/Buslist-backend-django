# BusList API - README PRINCIPAL

## Sumario
- [Visão Geral](#1-bustlist-api---visão-geral)
- [Sobre o Projeto](#2-sobre-o-projeto)
- [Tecnologias Utilizadas](#3-tecnologias-utilizadas)
- [Funcionalidades Principais](#4-funcionalidades-principais)
    - [User](#41-usuário-user)
    - [Student](#42-estudante-student)
    - [Bus](#43-ônibus-bus)
    - [Trip](#44-viagens-trips)
    - [Attendance](#45-presença-attendance)
- [Segurança](#5-segurança)
- [Arquitetura](#6-arquitetura)
- [Documentação](#7-documentação)
- [Objetivo do Projeto](#8-objetivo-do-projeto)

## 1. BustList API - Visão Geral

API REST desenvolvida para gerenciamento de transporte universitário, permitindo o controle de ônibus, estudantes, viagens e presença dos estudantes.

O projeto foi desenvolvido utilizando Django e Django REST Framework, com PostgreSQL como banco de dados e Docker para containerização da aplicação e do banco de dados.

## 2. Sobre o Projeto

O BusList é uma API REST desenvolvida para gerenciar o transporte de estudantes entre instituições de ensino.

A aplicação permite o gerenciamento de:

- Ônibus
- Estudantes
- Viagens
- Presença dos estudantes
- Usuários e administradores

A API possui autenticação baseada em JWT e controle de acesso aos recursos da aplicação.

O projeto utiliza uma arquitetura organizada em diferentes camadas, buscando manter as responsabilidades separadas e facilitar a manutenção e evolução do sistema.

## 3. Tecnologias Utilizadas

Backend
- Python 3.13
- Django 6.0.6
- Django REST Framework
- Simple JWT
- drf-spectacular

Banco de dados
- PostgreSQL 17.10
- Infraestrutura
- Docker
- Docker Compose

Ferramentas
- Postman
- DBeaver
- PgAdmin
- Git / GitHub

## 4. Funcionalidades Principais

### 4.1 Usuário (User)

- Registro de usuários;
- Autenticação utilizando JWT;
- Autenticação por e-mail;
- Controle de permissões;
- Definição de usuário como administrador.

### 4.2 Estudante (Student)

- Cadastro de estudantes;
- Listagem de estudantes;
- Busca por ID;
- Atualização de estudantes;
- Remoção de estudantes.

### 4.3 Ônibus (Bus)

- Cadastro de ônibus;
- Definição da capacidade;
- Validação da capacidade mínima;
- Ativação/desativação;
- Atualização de ônibus;
- Listagem de ônibus.

### 4.4 Viagens (Trips)

- Criação de viagens;
- Associação de ônibus à viagem;
- Associação de estudantes à viagem;
- Consulta de viagens;
- Controle dos estudantes vinculados à viagem.

### 4.5 Presença (Attendance)

- Registro de presença do estudante em viagens;
- Associação entre estudante e viagem;
- Controle da participação dos estudantes;
- Consulta dos registros de presença.

## 5. Segurança

A API utiliza autenticação baseada em JWT (JSON Web Token) para proteger os endpoints da aplicação.

A autenticação é realizada através do Django REST Framework em conjunto com o Simple JWT.

Principais recursos
- Autenticação utilizando JWT;
- Access Token com tempo de expiração configurado;
- Refresh Token;
- Autenticação através do header Authorization;
- Controle de acesso utilizando permissões do Django REST Framework;
- Usuário personalizado através de AUTH_USER_MODEL;
- Senhas armazenadas utilizando o sistema de hash do Django.

As requisições autenticadas devem enviar o token no seguinte formato:

Authorization: ```Bearer <access_token>```

A API utiliza permissões do Django REST Framework para determinar quais recursos podem ser acessados por usuários autenticados.

## 6. Arquitetura

O projeto segue uma arquitetura organizada em camadas, buscando separar responsabilidades e facilitar a manutenção, evolução e testes da aplicação.

A comunicação principal entre as camadas segue o fluxo:

```Request ->  View ->  Serializer ->  Service -> Django ORM -> PostgresSQL```

## 7. Documentação

Abaixo estão os documentos disponíveis:

| Documento                                     | Descrição                                                       |
|-----------------------------------------------|-----------------------------------------------------------------|
| [Guia de Arquitetura](./docs/architecture.md) | Guia informativo e de orientação sobre a arquitetura do projeto |
| [Guia de Instalação](./docs/installation.md)  | Instruções para configurar o ambiente local e executar o projeto |

## 8. Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

- Prática de desenvolvimento de APIs REST utilizando Django REST Framework;
- Implementação de autenticação e autorização utilizando JWT;
- Aplicação de uma arquitetura organizada em camadas;
- Utilização de uma Service Layer para centralização das regras de negócio;
- Prática com Django ORM e PostgreSQL;
- Containerização da aplicação utilizando Docker e Docker Compose;
- Desenvolvimento de uma API com estrutura próxima a um ambiente real de backend;
- Comparação e aplicação dos conceitos aprendidos anteriormente com Java e Spring Boot em uma nova stack tecnológica.