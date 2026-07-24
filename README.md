# 💰 Sistema de Controle Financeiro

Um sistema de controle financeiro desenvolvido em **Python** utilizando **SQLite3** para armazenamento dos dados.

O projeto foi criado com o objetivo de praticar conceitos de **Programação Orientada a Objetos (POO)**, **CRUD**, **SQLite3**, tratamento de exceções e consultas SQL.

---

## 📷 Funcionalidades

- ✅ Cadastrar transações
- 📋 Listar todas as transações
- 🔍 Buscar transação por ID
- ✏️ Atualizar uma transação
- 🗑️ Excluir uma transação
- 💵 Calcular saldo (Entradas - Saídas)
- 📊 Exibir gastos por categoria

---

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLite3
- SQL

---

## 📚 Conceitos praticados

- Programação Orientada a Objetos (POO)
- CRUD
- SQLite3
- SQL
- Funções de agregação (`SUM`)
- Agrupamento de dados (`GROUP BY`)
- Ordenação (`ORDER BY`)
- Tratamento de exceções (`try/except`)
- Validação de dados
- Organização do código em métodos

---

## 📂 Estrutura do banco de dados

Tabela:

```sql
transacoes
```

Campos:

| Campo | Tipo |
|--------|------|
| id | INTEGER |
| descricao | TEXT |
| valor | REAL |
| tipo | TEXT |
| categoria | TEXT |

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/controle-financeiro-python.git
```

### 2. Acesse a pasta

```bash
cd controle-financeiro-python
```

### 3. Execute o programa

```bash
python main.py
```

Na primeira execução, o banco de dados será criado automaticamente.

---

## 📌 Menu

```
===== CADASTRO DE TRANSAÇÃO =====

[1] Cadastrar transação
[2] Listar transações
[3] Buscar transação por ID
[4] Atualizar transação
[5] Excluir transação por ID
[6] Calcular saldo
[7] Gastos por categoria
[0] Sair
```

---

## 💡 Exemplo de uso

Cadastro:

```
Descrição: Salário
Valor: 3500
Tipo: Entrada
Categoria: Trabalho
```

Cadastro:

```
Descrição: Supermercado
Valor: 280
Tipo: Saída
Categoria: Alimentação
```

Resultado:

```
Total de entradas: R$ 3500.00
Total de saídas: R$ 280.00

Saldo atual: R$ 3220.00
```

---

## 🚀 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- Modelagem de dados
- Operações CRUD
- Persistência de dados com SQLite3
- Consultas SQL
- Programação Orientada a Objetos
- Organização de código
- Tratamento de erros
- Manipulação de banco de dados utilizando Python

---

## 🔮 Melhorias futuras

- Interface gráfica (Tkinter ou CustomTkinter)
- Interface Web com Flask
- Migração para PostgreSQL
- Relatórios mensais
- Filtro por período
- Pesquisa por categoria
- Exportação para CSV
- Dashboard financeiro
- Login de usuários

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Barbosa** como projeto de estudos em Python e Banco de Dados.

GitHub:
https://github.com/barbosa-06

LinkedIn:
(Adicione o link do seu LinkedIn)

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.
