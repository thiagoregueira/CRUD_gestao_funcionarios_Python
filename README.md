# Gestão de funcionários em python
Este é um sistema de gerenciamento de funcionários, implementado em Python. O sistema permite adicionar, listar, atualizar e remover funcionários, além de salvar e carregar dados de funcionários.

## Estrutura do Projeto

O projeto tem a seguinte estrutura de diretório:
```
.
├── __pycache__/
├── .gitignore
├── funcionarios_dados.pkl
├── funcionarios.py
├── main.py
├── requirements.txt
└── sistema_gestao.py`
```

## Descrição dos Arquivos

- `funcionarios.py`: Define a classe Funcionario, que representa um funcionário com nome, salário e departamento.
- `sistema_gestao.py`: Define a classe SistemaGestao, que gerencia uma lista de funcionários. Esta classe tem métodos para adicionar, listar, atualizar e remover funcionários, além de salvar e carregar dados de funcionários.
- `main.py`: Este é o ponto de entrada do programa. Ele cria uma instância de SistemaGestao, carrega os dados dos funcionários e entra em um loop de menu principal, onde o usuário pode escolher entre várias opções para gerenciar os funcionários.
- `requirements.txt`: Este arquivo lista as dependências do projeto.

## Como Executar

Para executar este projeto, siga estas etapas:

1. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
2. Execute o arquivo `main.py` com o comando `python main.py`.

