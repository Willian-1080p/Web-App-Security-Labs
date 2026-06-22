# SQL Injection

## Objetivo

Compreender vulnerabilidades de SQL Injection e métodos de mitigação.

## Descrição

SQL Injection ocorre quando entradas do usuário são inseridas diretamente em consultas SQL sem validação adequada.

## Exemplo Vulnerável

```sql
SELECT * FROM users WHERE username = '$user';
```

## Impactos

* Bypass de autenticação
* Vazamento de dados
* Alteração de registros
* Exclusão de informações

## Mitigações

* Prepared Statements
* Parameterized Queries
* Validação de Entrada
* Princípio do Menor Privilégio

## Ferramentas

* Burp Suite
* SQLMap
* OWASP ZAP

## Referência OWASP

A03:2021 – Injection
