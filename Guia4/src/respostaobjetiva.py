from typing import List, Tuple, Dict
from .resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, indice_escolhido: int):
        super().__init__(pergunta)
        self.indice_escolhido = indice_escolhido
        self.alternativa_selecionada = None
        self.esta_correta = self.pergunta.validar_resposta(self.indice_escolhido)
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0

    def calcular_pontuacao(self) -> float:
        return self.pontuacao_obtida