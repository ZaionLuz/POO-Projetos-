from typing import List, Tuple, Dict
from .resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, texto_resposta: str):
        super().__init__(pergunta)
        self.texto_resposta = texto_resposta
        self.esta_correta = bool(self.pergunta.validar_resposta(self.texto_resposta))
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0

    def calcular_pontuacao(self) -> float:
        return self.pontuacao_obtida