<h1 align="center">Urna Eletrônica</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-8a2be2?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-ff69b4?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Concluído-8a2be2?style=for-the-badge" />
</p>

<p align="center">
  Simulação de uma urna eletrônica no terminal, feita em Python com banco de dados SQLite:<br>
  cadastro de candidatos, votação com controle por CPF e apuração com porcentagens.
</p>

---

## Funcionalidades

- **Cadastro de candidatos**, um após o outro, até digitar `fim`
- **Votação** com escolha pelo número do candidato
- **Um voto por CPF**: o sistema recusa quem já votou
- **Apuração** com total de votos e porcentagem de cada candidato
- Anuncia o **eleito** ou avisa quando há **empate** (segundo turno)
- Os dados ficam salvos no banco, mesmo depois de fechar o programa

## Como funciona

```
==== MENU ====
1 - Cadastrar candidatos
2 - Votar
3 - Apurar votos
4 - Sair
```

Exemplo de apuração:

```
--- Apuração dos Votos ---
Maria - 4 votos (57.1%)
João - 3 votos (42.9%)

🎉 Eleito(a): Maria
```

## Banco de dados

O banco `urna_eletronica.db` é criado automaticamente na primeira execução.

```
 candidatos ──< votos
```

| Tabela       | Campos                                                         |
| :----------- | :------------------------------------------------------------- |
| `candidatos` | `id` (PK), `nome`                                               |
| `votos`      | `id` (PK), `candidato_id` (FK), `cpf` (**único**)               |

> A restrição `UNIQUE` no CPF garante, no próprio banco, que cada pessoa vote uma única vez.

## O que o projeto pratica

- Conexão com **SQLite** usando a biblioteca padrão `sqlite3`
- Criação de tabelas com chave primária, chave estrangeira e `UNIQUE`
- Consultas com parâmetros (`?`), que evitam **SQL Injection**
- `JOIN`, `GROUP BY` e `COUNT` para a apuração
- Menu interativo com `while`, funções e tratamento de erro com `try/except`
