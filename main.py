from dotenv import load_dotenv
import utils

import os

url = ""

#Exemplos de utilização
load_dotenv()
token_tela = utils.Token_tela(client_id=os.getenv('TOKEN_TELA_EXTENSOES_CLIENT_ID'),
                              token=os.getenv('TOKEN_TELA_EXTENSOES_BASE'),
                              scopes=[
                                  "campos-adicionais.suite",
                                  "contas-usuarios.suite",
                                  "dados.suite",
                                  "gerenciador-configuracoes.suite",
                                  "gerenciador-relatorios.suite",
                                  "gerenciador-scripts.suite",
                                  "licenses.suite",
                                  "modelo-dados.suite",
                                  "naturezas.suite",
                                  "notifications.suite",
                                  "quartz.suite",
                                  "sistema_interno",
                                  "user-accounts.suite"
                              ],
                              redirect_uri='https://scripts.plataforma.betha.cloud/auth-callback.html')

retorno = utils.RequisicaoTela(authorization=token_tela,
                                   method="GET",
                                   url=url,
                                   headers={
                                       'accept': 'application/json, text/plain, */*',
                                       'user-access': os.getenv("TOKEN_TELA_USER_ACCESS"),
                                       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
                                   }).rodar()

print(retorno.json())
