import json

import requests as rq


class Token_tela:
    def __init__(self, client_id, scopes, redirect_uri, token):
        self.client_id = client_id
        self.scopes = scopes
        self.redirect_uri = redirect_uri
        self.token = token

    def __str__(self):
        return 'Bearer ' + str(self.token)

    @property
    def dict_header(self):
        return {"authorization": str(self)}

    def refresh(self):
        new_token_retorno = rq.get(url="https://plataforma-oauth.betha.cloud/auth/oauth2/authorize",
                                   params={'client_id': self.client_id,
                                           'response_type': 'token',
                                           'redirect_uri': self.redirect_uri,
                                           'silent': 'true',
                                           'callback': '',
                                           'bth_ignore_origin': 'true',
                                           'previous_access_token': self.token
                                           })
        new_token_string = new_token_retorno.text
        new_token_formatado = new_token_string.replace("(", "").replace(")", "")
        new_token = json.loads(new_token_formatado).get("accessToken")
        self.token = new_token
        return new_token

    @property
    def info(self):
        request = rq.get(url='https://plataforma-oauth.betha.cloud/auth/oauth2/tokeninfo',
                         params={"access_token": self.token})
        return request.json()

    def valid(self):
        return not self.info.get("expired")
