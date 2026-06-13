from typing import List, Tuple, Dict
from .pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto: str, resposta_esperada: str = None, case_sensitive: bool = False, explicacao_geral: str = None):
        super().__init__(texto, explicacao_geral)
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive

    def validar_resposta(self, texto: str) -> bool:
        if self.resposta_esperada is None:
            return False

        if self.case_sensitive:
            return texto == self.resposta_esperada

        return texto.strip().lower() == self.resposta_esperada.strip().lower()

    def get_tipo(self):
        return "discursiva"