# Servidor csvs

#### Criando arquivos .env
Crie o arqivo .env e o .env.example na pasta do servidor com as seguintes variáveis:
```
SECRET= 
USUARIO=
SENHA=
```
Exemplo:
```
SECRET='asdgghexxh123';
USUARIO=jair
SENHA=123
```

#### Build do docker
Para rodar o servidor usando docker compose primeiro você deve dar o build na imagem realizando o seguinte comando:
```
docker-compose build
```

#### Rodar o docker
Para rodar utilizar o comando:
```
docker-compose run -p 8080:8080 servidor_csvs
```

Então o seu servidor estará rodando na porta 8080

#### Para logar

Acessar a url http://localhost:8080/login/ passando os parâmetros user e pwd, no postman você pode adicionar
esses parâmetros no body e realizar um POST

#### Para acessar o csv

Para ter acesso aos csvs entre na url: http://localhost:8080/csvs/ passando o token gerado no momento do login,
no postman você pode adicionar esse parâmetro como x-access-token.
