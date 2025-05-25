# 🌐 Rede AMADO - Backend com FastAPI

Este é o backend da plataforma **Rede AMADO**, um sistema informativo e interativo com foco em atendimentos, serviços, blog, loja e contatos, desenvolvido com **FastAPI** e **SQLite**.

## 🚀 Tecnologias utilizadas

- **Python 3.10+**
- **FastAPI** — framework web moderno e rápido
- **Uvicorn** — servidor ASGI leve para FastAPI
- **SQLAlchemy** — ORM para manipulação do banco de dados
- **SQLite** — banco de dados leve e local
- **Pydantic** — validação de dados com tipagem forte

## 📁 Estrutura do Projeto

rede_amado/
├── main.py # Arquivo principal do FastAPI
├── database.py # Conexão com o banco de dados
├── models.py # Modelos do banco de dados (SQLAlchemy)
├── schemas.py # Esquemas de entrada/saída (Pydantic)
└── routers/
    ├── atendimento.py # Rotas de atendimento
    ├── usuario.py # Rotas de usuários
    ├── produto.py # Rotas da loja
    ├── blog.py # Rotas de blog/eventos
    ├── servico.py # Rotas de serviços
    └── contato.py # Rotas de contato


## 🧪 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/rede_amado.git
cd rede_amado
``` 

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode o servidor
```bash
uvicorn backend.main:app --reload
```
Acesse em: ´http://127.0.0.1:8000´

### 5. Documentação automática

Swagger UI: `http://127.0.0.1:8000/docs`

## 📌 Funcionalidades implementadas

- CRUD de Atendimentos
- CRUD de Contato
- CRUD de Serviços
- CRUD de Blog/Eventos
- CRUD de Loja (Produtos)
- CRUD de Usuários (Voluntários e Público)
- Conexão com banco SQLite
- Documentação automática com Swagger

## ✨ Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar issues ou pull requests.

© 2025 Rede AMADO. Todos os direitos reservados.