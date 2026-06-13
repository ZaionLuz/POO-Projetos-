from typing import List, Tuple, Dict
from .pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto: str, alternativas: list, explicacao_geral: str = None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas

    def validar_resposta(self, indice: int) -> bool:
        if indice < 0 or indice >= len(self.alternativas):
            return False
        return self.alternativas[indice].correta

    def get_alternativa_correta(self):
        for alt in self.alternativas:
            if alt.correta:
                return alt
        return None

    def get_tipo(self):
        return "multipla_escolha"