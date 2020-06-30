# gaviao
 
## Inicializar o API

A inicialização do servidor consiste nos seguintes passos:

1. Ambiente virtual
2. Instalação de requisitos
3. Iniciar o servidor

Os passos aqui descritos foram efectuados em Windows 10.

### Criação de ambiente virtual

Antes de correr o servidor, é necessário a utilização de um ambiente virtual de Python. Para isso pode ser usado pacote `venv` ou o comando `conda`.

PIP:
```
pip install virtualenv
python -m venv nome_do_ambiente
cd ./nome_do_ambiente/Scripts
./activate
```

conda:
```
conda create -n nome_do_ambiente
conda activate nome_do_ambiente
```

Em ambos os casos, para sair do ambiente virtual:

```
deactivate
```
