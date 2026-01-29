# Especificação de Requisitos – Django ToDoList

## 1. Introdução

Esta documentação apresenta a especificação técnica da aplicação Django ToDoList, destinada a equipas técnicas envolvidas no desenvolvimento, QA, segurança e treinamento. O objetivo é fornecer uma referência clara sobre requisitos, casos de uso, modelos de dados, navegação e interfaces, garantindo alinhamento entre todas as áreas envolvidas.

## 2. Descrição da Aplicação

A Django ToDoList é uma aplicação web para gestão de tarefas pessoais, oferecendo funcionalidades como registo e autenticação de utilzadores, operações CRUD de tarefas e associação de tarefas ao utilizador autenticado. Os principais ativos contemplam credenciais, dados das tarefas, sessões autenticadas e a base de dados.

Registo e autenticação de utilizadores

CRUD de tarefas vinculado ao utilizador

Gestão de sessões autenticadas

Proteções básicas de segurança

## 3. Requisitos Funcionais

RF01: Registo de utilizadores

RF02: Login e logout

RF03: Criação de tarefas

RF04: Listagem de tarefas do utilizador autenticado

RF05: Edição de tarefas próprias

RF06: Eliminação de tarefas próprias

RF06: Alteração de Estado (Pendente, Concluída) de tarefas próprias

## 4. Casos de Uso

![image1.png](images/image1.png)

UC01 – Registar Utilizador: permite criar utilizador com permissões para aceder ao sistema de gestão de tarefas.

UC1 – Autenticar Utilizador: permite acesso ao sistema mediante credenciais válidas.

UC2 – Registar tarefa: utilizador autenticado pode registrar novas tarefas.

UC3 – Gerir tarefas: permite gerir exclusivamente as tarefas do utilizador logado:

UC3.1 – Editar tarefa

UC3.2 – Eliminar tarefa

UC3.3. – Alterar estado tarefa (Pendente, Concluída)

UC5 – Logout: permite encerrar a sessão e retornar ao ecrã de Login.

## 5. Quadro Explicativo dos Casos de Uso

## 7. Dicionário de Dados 

A estrutura da tabela de Tarefas está representada abaixo:

![image2.png](images/image2.png)

## 8. Navegação da Aplicação

Ecrã de Registo: Cadastro de novo utilizador.

Ecrã de Login: Utilizador insere credenciais para acessar o sistema.

Ecrã Principal: Exibe lista de tarefas do utilizador autenticado.

Ecrã de Criação/Edição de Tarefa: Formulário para inserir ou alterar dados da tarefa.

Fluxo: Após login, utilizador é redirecionado à lista de tarefas, podendo navegar para criar, editar ou apagar tarefas.

## 9. Desenho das Interfaces

### 1. Login:

Campos: utilizador, password

Botão: Entrar

![image3.png](images/image3.png)

Link: Registo de novo utilizador

### 2. Gestão de Tarefas:

Exibição em tabela: título, Estadi, ações (alternar, editar, apagar)

Botão: Nova tarefa

![image4.png](images/image4.png)

### 3. Criação/Edição:

Campos: título, descrição

Botões: Guardar

![image5.png](images/image5.png)


## Imagens Extraídas
![image1.png](images/image1.png)

![image2.png](images/image2.png)

![image3.png](images/image3.png)

![image4.png](images/image4.png)

![image5.png](images/image5.png)

