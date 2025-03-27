import requests
import utils.requisicoes_tela.Token_tela

class RequisicaoTela:

    def __init__(self, authorization: utils.requisicoes_tela.Token_tela, method=None, url=None, data=None, headers={}, files=None, json=None, params=None):
        """
        :type Token_tela
        :type data: Any
        :type method: str
        :type headers: class headers
        :type url: str
        :type files: files
        :type params: dict
        :type json: str(json)
        """
        self.authorization = authorization
        self.method = method
        self.url = url
        self.data = data
        self.files = files
        self.json = json
        self.params = params
        self.headers = headers
        self._refreshed_token = False

    def rodar(self, method=False, url=False, data=False, headers={}, files=False, json=False, params=False):
        argumentos = {'method': method if method != False else self.method,
                      'url': url if url != False else self.url,
                      'headers': {**(headers if headers not in ({},None) else self.headers),**self.authorization.dict_header},
                      'data': data if data != False else self.data,
                      'files': files if files != False else self.files,
                      'json': json if json != False else self.json,
                      'params': params if params != False else self.params}
        requisicao = requests.request(**argumentos)
        if not requisicao.ok and \
                requisicao.status_code == 401 and \
                not self._refreshed_token:
            self._refreshed_token = True
            self.authorization.refresh()
            requisicao = self.rodar(**argumentos)

        self._refreshed_token = False
        return requisicao
