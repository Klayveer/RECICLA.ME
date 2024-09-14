# Projeto Interdisciplinar: Gestão de Resíduos Sólidos

Este projeto foi desenvolvido como parte de um trabalho interdisciplinar de Engenharia da Computação, abordando as disciplinas de Programação de Sistemas Especialistas, Análise Orientada a Objetos (OO) e Modelagem e Simulação Matemática. O objetivo é criar um sistema especialista para otimizar a coleta e o tratamento de resíduos sólidos, utilizando um dataset real da empresa Cascais Ambiente.

## Objetivo

Desenvolver um sistema que analisa e prevê a geração de resíduos sólidos com base em dados históricos, utilizando Python, APIs, modelagem matemática, simulação e visualização gráfica. O sistema será capaz de fornecer previsões e gerar gráficos interativos para auxiliar no planejamento da coleta e destinação dos resíduos.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **API REST**: Criada com FastAPI para comunicação com outros sistemas e consulta de dados.
- **Machine Learning**: Técnicas para prever a geração futura de resíduos.
- **Modelagem Matemática e Simulação**: Para prever a quantidade de resíduos sólidos no futuro.
- **Bibliotecas Gráficas**: `matplotlib`, `seaborn`, ou `plotly` para visualizações interativas.
- **Diagramas UML**: Para modelagem e documentação das classes e interações do sistema.

## Funcionalidades

1. **Análise de Resíduos**: Relatórios detalhados por categoria de resíduos.
2. **Previsão de Resíduos**: Previsões com base nos dados históricos usando métodos estatísticos e machine learning.
3. **Visualização Gráfica**: Gráficos que mostram o comportamento dos resíduos ao longo do tempo e previsões.
4. **API REST**: Inserção e consulta de novos dados de resíduos por meio de uma API.
5. **Simulação**: Simulação de coleta e geração futura de resíduos.

## Dataset

O dataset utilizado contém dados diários da quantidade de resíduos sólidos recolhidos pela empresa Cascais Ambiente, divididos nas seguintes categorias:

- Cortes de Jardim
- Objetos Fora de Uso
- Óleos Alimentares Usados
- Papel/Cartão
- Plástico/Metal
- Recolha Indiferenciada
- Resíduos de Limpeza
- Resíduos Urbanos Biodegradáveis
- Vidro

## Arquitetura

### Diagrama UML (Esboço)

```plaintext
+-------------------+            +---------------------+
|     Classe API     | -------> |   Classe Resíduos   |
+-------------------+            +---------------------+
         |                             |
         v                             v
+-------------------+            +---------------------+
|  Classe Simulação  | -------> |    Classe Gráfico    |
+-------------------+            +---------------------+
```

## Classes Principais

- **Residuos:** Responsável por ler, armazenar e processar os dados do dataset.
- **Categoria:** Representa cada categoria de resíduos (ex.: Papel/Cartão, Plástico/Metal).
- **Simulacao:** Implementa métodos para simulação e previsão da coleta futura de resíduos.
- **Grafico:** Gera gráficos interativos com os dados históricos e previsões.
- **API:** Facilita a integração e comunicação com outros sistemas via requisições HTTP.

## Instalação

Clone o repositório:

```bash
git clone [https://github.com/Klayveer/AV3](https://github.com/Klayveer/AV3)
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python main.py
```

## Para acessar a API (usando FastAPI):

Acesse a documentação da API via `http://127.0.0.1:8000/docs`

## Como Usar

- **Inserir novos dados**: Utilize a rota `/api/v1/residuos` para inserir novos dados de resíduos.
- **Consultar previsões**: Acesse a rota `/api/v1/simulacao` para obter previsões de geração de resíduos.
- **Visualizar gráficos**: Execute o módulo de gráficos `grafico.py` para gerar visualizações dos dados.

## Modelagem Matemática e Simulação

Utilizamos técnicas de regressão linear e outros métodos estatísticos para prever a quantidade de resíduos sólidos gerados no futuro. A simulação ajuda a prever a melhor frequência de coleta para diferentes categorias de resíduos, com base nos dados históricos.

## Contribuições

1. Fork o projeto.
2. Crie uma nova branch `(git checkout -b feature/nova-funcionalidade)`.
3. Faça suas alterações e commit `(git commit -m 'Adiciona nova funcionalidade')`.
4. Envie para o repositório original `(git push origin feature/nova-funcionalidade)`.
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
