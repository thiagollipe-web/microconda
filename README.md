# MicroConda Studio

<div align="center">

<img src="./icons/microconda.svg" width="128" alt="MicroConda logo">

# MicroConda

**Um ambiente Python leve, educativo e instalável como PWA, direto no navegador.**

[**Abrir MicroConda Studio**](https://thiagollipe-web.github.io/microconda/)

</div>

---

## Visão geral

O MicroConda Studio transforma o navegador em um pequeno ambiente de desenvolvimento Python. A proposta é permitir que o usuário escreva, execute e organize código sem instalar um IDE tradicional.

O projeto utiliza **Pyodide/WebAssembly** para executar Python no navegador e possui uma interface responsiva pensada para desktop e celular.

## O que já existe

- Editor Python com numeração de linhas.
- Terminal REPL integrado.
- Execução com Ctrl + Enter.
- Projetos com múltiplos arquivos .py.
- Persistência local do projeto no navegador.
- Criação de novos arquivos.
- Exemplos prontos de Python.
- Download de arquivos .py.
- Exportação do projeto em JSON.
- Histórico de comandos do terminal.
- Comandos help, clear, version, files e load(...).
- Instalação de pacotes Python compatíveis via micropip.
- Exemplo de Space Invaders ASCII executado pelo terminal.
- Interface responsiva para telas menores.
- Manifesto e instalação como PWA.
- Logo e identidade visual próprias.

## Como o projeto funciona

```text
┌──────────────────────────────┐
│       MicroConda Studio      │
├───────────┬──────────┬───────┤
│ Projeto   │ Editor   │Terminal│
│ arquivos  │ Python   │ REPL   │
└───────────┴─────┬────┴───────┘
                  │
                  ▼
          Pyodide / WebAssembly
                  │
                  ▼
             Python no browser
```

O aplicativo é essencialmente client-side: o código Python é enviado ao runtime Pyodide dentro do navegador.

## Interface desktop

<img src="./docs/screenshots/microconda-studio-desktop.svg" alt="MicroConda Studio desktop" width="100%">

## Interface mobile

<img src="./docs/screenshots/microconda-studio-mobile.svg" alt="MicroConda Studio mobile" width="420">

## Exemplo: Space Invaders ASCII

Um dos testes do ambiente é um pequeno jogo ASCII escrito em Python. Ele demonstra que o terminal pode executar lógica de jogo além de scripts simples.

<img src="./docs/screenshots/space-invaders-ascii.svg" alt="Space Invaders ASCII no MicroConda" width="100%">

Controles:

```text
A = esquerda
D = direita
F = atirar
Q = sair
```

## PWA

O MicroConda possui manifest.webmanifest, ícone próprio, Service Worker, modo standalone e botão de instalação quando o navegador disponibiliza a instalação.

Em navegadores compatíveis, o aplicativo pode ser instalado na tela inicial do celular ou no desktop.

> **Importante:** o shell do PWA possui cache local, mas o runtime Pyodide é carregado de uma CDN. Portanto, a instalação como PWA não significa que a execução de Python esteja totalmente offline em uma nova instalação.

## Testar

Acesse: **https://thiagollipe-web.github.io/microconda/**

No celular, abra no Chrome ou outro navegador compatível e utilize a opção **Instalar aplicativo** quando disponível.

## Estrutura principal

```text
microconda/
├── index.html
├── manifest.webmanifest
├── sw.js
├── icons/
│   └── microconda.svg
├── docs/
│   └── screenshots/
│       ├── microconda-studio-desktop.svg
│       ├── microconda-studio-mobile.svg
│       └── space-invaders-ascii.svg
├── space_invaders_ascii.py
├── miniconda-installer.sh
└── LICENSE
```

## Tecnologias

| Tecnologia | Função |
|---|---|
| HTML5 | Interface |
| CSS3 | Layout responsivo |
| JavaScript | IDE, terminal e integração |
| Python | Linguagem executada |
| Pyodide | Python via WebAssembly |
| PWA | Instalação como aplicativo |
| Service Worker | Cache do shell |
| LocalStorage | Persistência local |

## Estado do projeto

O projeto está em evolução, com foco em um Python Studio educacional e mobile-first.

## Licença

Este projeto mantém a licença presente no arquivo LICENSE.

<div align="center">
**MicroConda Studio · Python no navegador**
</div>