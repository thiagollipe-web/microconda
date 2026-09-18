# MicroConda Browser Python

Um terminal/IDE Python que roda diretamente no navegador.

## Como funciona

O arquivo `index.html` usa [Pyodide](https://pyodide.org/) para executar CPython compilado para WebAssembly. A versão estável usada nesta implementação é a 314.0.7, publicada pelo projeto Pyodide em setembro de 2026. O Pyodide permite executar Python e carregar pacotes compatíveis dentro do navegador. 

A interface inclui:
- editor `main.py`;
- execução com Ctrl+Enter;
- terminal interativo;
- histórico de comandos;
- saída de `print()` e erros;
- salvamento do código no navegador;
- download do programa como `.py`;
- instalação de pacotes compatíveis via `install("nome-do-pacote")`;
- reset do ambiente Python.

## Executar

Abra o `index.html` em um servidor estático ou publique o repositório no GitHub Pages.

Exemplos no terminal:

```python
print("Olá, mundo!")
```

```python
import math
print(math.sqrt(81))
```

Para instalar um pacote compatível:

```python
await install("numpy")
import numpy as np
print(np.arange(5))
```

## Importante

O `miniconda-installer.sh` continua sendo um instalador Linux e não pode ser executado diretamente pelo navegador. O terminal web usa Pyodide/WebAssembly para fornecer Python dentro da página. Para executar um ambiente Conda/Miniconda real, com acesso ao sistema operacional e aos pacotes nativos do computador, é necessário um backend ou uma instalação local.

