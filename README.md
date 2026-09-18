# MicroConda Game Studio

<div align="center">

<img src="./icons/microconda.svg" width="128" alt="MicroConda logo">

# MicroConda

**Um estúdio leve para criar jogos em HTML, CSS e JavaScript diretamente no navegador.**

[**Abrir MicroConda Game Studio**](https://thiagollipe-web.github.io/microconda/)

</div>

---

## Visão geral

O MicroConda Game Studio transforma o navegador em um ambiente simples para criação e teste de jogos 2D. O editor trabalha com **HTML, CSS e JavaScript**, com visualização em **Canvas** e foco em uso mobile.

O projeto é **client-side** e salva o projeto no `LocalStorage` do próprio navegador.

## Recursos

- Editor com numeração de linhas.
- Projetos com arquivos `.html`, `.css` e `.js`.
- Execução imediata no painel de jogo.
- Pré-visualização isolada em `iframe` com sandbox.
- Suporte a interação por toque e ponteiro.
- Histórico simples do console.
- Persistência automática no navegador.
- Criação de novos arquivos.
- Exportação do jogo como **um único arquivo HTML**.
- Abertura do jogo em uma nova janela.

## Fluxo do projeto

```text
MicroConda Game Studio
        │
        ├── HTML
        ├── CSS
        └── JavaScript
              │
              ▼
          Canvas / DOM
              │
              ▼
       Pré-visualização do jogo
              │
              ▼
      Exportação: jogo.html
```

O arquivo `index.html` funciona como a interface completa do Studio. Os arquivos criados pelo usuário ficam armazenados localmente no navegador.

## Interface

<img src="./docs/screenshots/microconda-studio-desktop.svg" alt="MicroConda Game Studio desktop" width="100%">

No celular, a interface reorganiza editor, projeto, console e área de jogo para caber na tela.

## Criando um jogo

O projeto inicial contém um exemplo mínimo em Canvas. Edite o arquivo `index.html` e clique em **▶ Executar** ou em **🎮 Executar jogo**.

Para projetos com mais arquivos, crie arquivos `.css` e `.js`. O Studio incorpora esses arquivos na pré-visualização e, ao exportar, reúne o conteúdo em um único HTML.

O jogo executado pelo Studio fica dentro de um `iframe` sandbox. Isso permite testar código do usuário sem misturá-lo diretamente com a interface do editor.

## Exportação

Use **Baixar HTML** ou **Exportar jogo** para gerar um arquivo `.html` autocontido.

O arquivo exportado reúne:

- HTML do projeto.
- CSS dos arquivos `.css`.
- JavaScript dos arquivos `.js`.

Não é necessário gerar ZIP ou estrutura de pastas para executar o jogo exportado.

## Armazenamento

O projeto é salvo automaticamente no armazenamento local do navegador usando a chave:

```text
microconda-game-studio-v1
```

Os dados permanecem no navegador/dispositivo usado para criar o projeto.

## Testar

Acesse:

https://thiagollipe-web.github.io/microconda/

No celular, use o navegador normalmente. Para jogar em uma janela dedicada, use **↗ Abrir jogo em janela** dentro do painel de jogo.

## Estrutura principal

```text
microconda/
├── index.html
├── icons/
│   └── microconda.svg
├── docs/
│   └── screenshots/
│       └── microconda-studio-desktop.svg
├── tests/
│   └── browser-smoke.mjs
├── .github/
│   └── workflows/
│       └── validate.yml
└── LICENSE
```

## Tecnologias

| Tecnologia | Função |
|---|---|
| HTML5 | Interface e estrutura dos jogos |
| CSS3 | Layout responsivo e estilos |
| JavaScript | Editor, execução, persistência e exportação |
| Canvas | Renderização de jogos 2D |
| LocalStorage | Salvamento local |
| iframe sandbox | Isolamento da pré-visualização |

## Estado do projeto

O MicroConda Game Studio está direcionado para uma experiência **mobile-first**, simples e local, com foco em prototipação de jogos e exportação de arquivos HTML independentes.

## Licença

Este projeto mantém a licença presente no arquivo `LICENSE`.

<div align="center">

**MicroConda Game Studio · HTML · CSS · JavaScript · Canvas**

</div>