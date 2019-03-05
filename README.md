# Flask Microservice Example

Um exemplo de um serviço flask usando rest-plus.

## Como começar?

1. Clone  repositório.

### Para virtualenv
* Crie um virtualenv com Python 3.7
* Ative o virtualenv.
* Instale o pipenv ```pip install pipenv``
* Instale as dependências usando o comando ```pipenv install``
* Configure a instância com o .env
*  Execute os testes.

``` console
git clone git@github.com:jonatasoli/example-flask-restplus.git example-flask-restplus
cd example-flask-restplus
python -m venv .example-flask-restplus
source .example-flask-restplus/bin/activate
pip install pipenv
pipenv install
cp contrib/env-sample .env
pytest -v --disable-pytest-warnings

```
### Para docker-compose - não funciona ainda
* Faça o build da aplicação ```docker-compose build``
* Rode os testes ```docker-compose run --rm app sh -c "pytest -v --disable-pytest-warnings"``
* Execute a aplicação ```docker-compose run --rm app sh -c "flask run"``

2. Ir até a aplicação CORE e remover a extenção example
3. Ir até factories/app_factory.py remover o blueprint relacionado a url example
4. Ir até o arquivo tests/test_example.py e remove-lo
5. Iniciar o desenvolvimento da sua aplicação


## Routes
Para capturar as rotas existentes usar o comando abaixo.
```
flask routes
```

## Deploy no Kubernetes
Para fazer o deploy da aplicação é necessário configurar os dois arquivos abaixo:
* staging-deployment.yml
* production-deployment.yml

Importante não esquecer de renomear o nome do pod e a url do container.

## Criar uma imagem no repositório do GCP
Para conseguir criar uma imagem no repositório do GCP primeiro precisamos instalar e configurar a ferramenta de linha de comando do google, depois é necessário rodar os comandos abaixo:

``` console
docker build . -t app --no-cache
docker tag app grc.io/my-project/{my-app-name}:latest
docker push -- grc.io/partyou-1f358/{my-app-name}:latest

```
Com isso já é possivel usar a imagem para montar pipelines no codefresh
