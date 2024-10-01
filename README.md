# LSL-931

# Projeto FastAPI com SQLAlchemy, Alembic e SlowAPI

Este projeto é uma API simples desenvolvida com FastAPI, SQLAlchemy, Alembic e SlowAPI. Ele permite a criação, leitura, atualização e exclusão de itens em um banco de dados MySQL via XAMPP, com limitação de taxa nas requisições.

## Funcionalidades

- **Cadastro de Itens**: Permite adicionar novos itens ao banco de dados.
- **Leitura de Itens**: Permite recuperar informações de um item pelo seu ID.
- **Atualização de Itens**: Permite atualizar informações de um item existente.
- **Exclusão de Itens**: Permite excluir um item existente.
- **Limitação de Taxa**: Utiliza SlowAPI para limitar o número de requisições por minuto para cada endpoint da API.
- **Controle Transacional**: Garante a integridade dos dados em operações de escrita.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção de APIs.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Alembic**: Ferramenta de migração de banco de dados.
- **SlowAPI**: Biblioteca para limitação de taxa de requisições.
- **MySQL**: Banco de dados relacional utilizado via XAMPP.
- **Pydantic**: Biblioteca para validação e conversão de dados.

## Configuração do Projeto

### Instalação

1. Clone o repositório:
   
```bash
    git clone https://github.com/Klayveer/LogicaDeProgramacao-Python
    cd Projeto_FastApi
```

2. Crie um ambiente virtual e ative-o:

```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows, use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
    pip install -r requirements.txt
```

### Configuração do Banco de Dados

1. Inicie o MySQL via XAMPP:

Abra o XAMPP e inicie o módulo MySQL.

2. Crie o Banco de Dados:

Acesse `phpMyAdmin` via `http://localhost/phpmyadmin` e crie um banco de dados chamado `fastapi_db`.

3. Configure a Conexão no Projeto:

No arquivo `app/database.py`, configure a URL de conexão para MySQL:

```python
    DATABASE_URL = "mysql://root@localhost:3306/fastapi_db"
```

4. Migrar o Banco de Dados:

Para garantir que o banco de dados está atualizado com as últimas alterações no modelo, execute:

```bash
    python -m alembic upgrade head
```

### Rodando o Servidor

Para iniciar o servidor FastAPI, use:

```bash
    python -m uvicorn app.main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`.

### Endpoints da API

Cadastro de Itens:
- Método: POST
- URL: `/items/`
- Limite de Requisições: 5 por minuto
- Corpo da Requisição:

```json
{
    "name": "Nome do Produto",
    "description": "Descrição do Produto",
    "price": 99.99
}
```

- Resposta:

```json
{
    "id": 1,
    "name": "Nome do Produto",
    "description": "Descrição do Produto",
    "price": 99.99
}
```

Leitura de Itens:
- Método: GET
- URL: `/items/{item_id}`
- Limite de Requisições: 5 por minuto
- Parâmetros: `item_id` - ID do item que deseja consultar.

Resposta:

```json
{
    "id": 1,
    "name": "Nome do Produto",
    "description": "Descrição do Produto",
    "price": 99.99
}
```

Atualização de Itens:
- Método: PUT
- URL: `/items/{item_id}`
- Limite de Requisições: 5 por minuto
- Corpo da Requisição:

```json
{
    "name": "Nome Atualizado",
    "description": "Descrição Atualizada",
    "price": 109.99
}
```

Resposta:

```json
{
    "id": 1,
    "name": "Nome Atualizado",
    "description": "Descrição Atualizada",
    "price": 109.99
}
```

Exclusão de Itens:
- Método: DELETE
- URL: `/items/{item_id}`
- Limite de Requisições: 5 por minuto

Resposta:

```json
{
    "mensagem": "Item deletado com sucesso"
}
```

### Estrutura do Projeto

```markdown
Projeto_FastApi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── alembic/
│   ├── versions/
│   ├── script.py.mako
│   └── env.py
├── .gitignore
├── README.md
├── requirements.txt
└── alembic.ini  
```

- main.py: Define as rotas da API.
- models.py: Define os modelos de dados.
- schemas.py: Define os schemas de validação de dados.
- crud.py: Contém funções de CRUD para interagir com o banco de dados.
- database.py: Configura a conexão com o banco de dados.

### Contribuições

Sinta-se à vontade para contribuir com melhorias. Se você encontrar problemas ou tiver sugestões, crie um issue ou envie um pull request.

### Licença
Este projeto está licenciado sob a MIT License.