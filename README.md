# Catálogo de Produtos e Categorias

Microserviço responsável pelo gerenciamento do catálogo de produtos e categorias, seguindo o padrão Clean Architecture para garantir modularidade, escalabilidade e manutenção fácil.

## Tecnologias Utilizadas

- **Framework:** Flask
- **Autenticação:** JWT (JSON Web Tokens)
- **Banco de Dados:** MySQL e SQLalchemy
- **Mensageria:** RabbitMQ (para comunicação assíncrona entre serviços)

#### Serviço de Catálogo

[![Continuos Integration -Testing, Build and Deploy Backend Catalog Microservice](https://github.com/maxsonferovante/catalog-microservice/actions/workflows/workflowTestingAndDeploy.yaml/badge.svg)](https://github.com/maxsonferovante/catalog-microservice/actions/workflows/workflowTestingAndDeploy.yaml)

- **Gerenciamento de Produtos:**
  - CRUD (Create, Read, Update, Delete) de produtos.
  - Atributos do produto: nome, descrição, preço, estoque, imagens, categorias, etc.
- **Gerenciamento de Categorias:**
  - CRUD de categorias.
  - Associação de produtos a categorias.
- **Busca e Filtragem:**
  - Pesquisa de produtos por nome, descrição e categoria.
  - Filtragem por preço, disponibilidade e outros atributos.

