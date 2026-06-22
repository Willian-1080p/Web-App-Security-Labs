# XSS

## Objetivo

Estudar ataques Cross-Site Scripting.

## Tipos

### Reflected XSS

Payload retornado imediatamente ao navegador.

### Stored XSS

Payload armazenado no servidor.

### DOM Based XSS

Manipulação insegura do DOM.

## Exemplo

```html
<script>alert('XSS')</script>
```

## Impactos

* Roubo de sessão
* Captura de credenciais
* Redirecionamento malicioso

## Mitigações

* Escape de saída
* CSP
* Sanitização de entrada
* HttpOnly Cookies

## Ferramentas

* Burp Suite
* OWASP ZAP
* Browser Developer Tools

## Referência OWASP

A03:2021 – Injection
