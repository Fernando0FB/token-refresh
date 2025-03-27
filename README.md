
## Instale os requisitos 
```bash
  pip install -r requirements.txt
```

## Preenchimento de informações do arquivo .env
No arquivo [.env](.env), deve ser inseridas informações da base do usuário, conforme informações abaixo:
```
TOKEN_TELA_EXTENSOES_CLIENT_ID= EntityId
TOKEN_TELA_EXTENSOES_BASE= Bearer Token atual
TOKEN_TELA_USER_ACCESS= USER_ACCESS do usuário
```

## Exemplo de utilização
O arquivo [.main.py](.main.py) possui um exemplo de utilização, tanto de getToken, quanto de realização da requisição em si.

