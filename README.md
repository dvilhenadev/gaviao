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

### Instalação de requisitos

Com o ambiente virtual criado e activado, podemos instalar os requisitos. Após clonar o repositório, entrar no seu diretório e utilizar `pip` para instalar os requisitos:

```
git clone https://github.com/dfvilhena/gaviao
cd ./gaviao
pip install -r requirements.txt
```

### Iniciar o servidor

Para iniciar o servidor, basta correr:

```
python manage.py runserver
```

Aceder à página <http://127.0.0.1:8000> resulta em erro 404. As páginas disponíves são:

Painel de administrador:
<http://127.0.0.1:8000/admin>

Pure Django:
<http://127.0.0.1:8000/report>

REST API:
<http://127.0.0.1:8000/api/report>

## Utilização do API

### Criação de utilizadores

Para criar novos utilizadores é necessário utilizar o painel de administrador. Basta aceder ao grupo 'Users' e adicionar novo utilizador.

### Visualização e criação de ocorrências

Acedendo a <http://127.0.0.1:8000/api/report> é fornecida a lista completa de ocorrências reportadas. Nesta página é também possível criar uma nova ocorrência utilizando o formulário no fundo da página. Neste momento existe 4 ocorrências na base de dados.

Aquando da criação de uma ocorrência, os seguintes campos são preenchidos automaticamente:
- author: preenchido com o username do utilizador
- creation_date: preenchido com a data e hora do momento de criação
- update_date: semelhante a creation_date, este campo é posteriormente actualizado
- status: o valor default é "Por validar", podendo no entanto ser alterado

### Actualização de ocorrências

Seguindo o endereço <http://127.0.0.1:8000/api/report/1> mostrará apenas a ocorrência 1. Alterando o valor a seguir a report/, mudará qual a ocorrência a apresentar. Nesta página é possível actualizar os campos.

Os seguintes campos são editáveis na actualização:
- description
- status
- location
- category

O campo `update_date` é atualizado com a data e hora do momento de atualização do relatório de ocorrência.

### REST Endpoints e Métodos HTTP

Os seguintes endpoints foram testados com os métodos especificados:

-   <http://127.0.0.1:8000/api/report/> - GET, POST
-   <http://127.0.0.1:8000/api/report/1> - GET

Exemplos de queries:
-   <http://127.0.0.1:8000/api/report/?a=admin> - GET, retorna todas as ocorrências que contenham 'admin' no campo `author`
-   <http://127.0.0.1:8000/api/report/?c=weather> - GET, retorna todas as ocorrências que contenham 'weather' no campo `category`
-   <http://127.0.0.1:8000/api/report/?l=sintra> - GET, retorna todas as ocorrências que contenham 'sintra' no campo `location`

É também possível juntar queries:

-   <http://127.0.0.1:8000/api/report/?c=weather&a=admin> - GET




# ToDo

- Localização com base em PostGIS ou Spatialite
- Query de localização com PostGIS
- Mostrar mapa com ocorrências