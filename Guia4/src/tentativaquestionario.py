from typing import List, Tuple, Dict
from datetime import datetime
from .respostaobjetiva import RespostaObjetiva
from .respostadiscursiva import RespostaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario: str):
        self.questionario = questionario
        self.usuario = usuario
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.respostas = []
        self._finalizado = False

    def registrar_resposta(self, indice_pergunta: int, valor):
        if self._finalizado:
            return

        pergunta = self.questionario.perguntas[indice_pergunta]

        if hasattr(pergunta, "alternativas"):
            resposta = RespostaObjetiva(pergunta, int(valor))
        else:
            resposta = RespostaDiscursiva(pergunta, str(valor))

        resposta.calcular_pontuacao()
        self.respostas.append(resposta)

    def calcular_pontuacao(self):
        return sum(r.pontuacao_obtida for r in self.respostas)

    def finalizar(self):
        self.data_fim = datetime.now()
        self._finalizado = True
        pontuacao = self.calcular_pontuacao()
        feedback = f"Usuário {self.usuario} fez {pontuacao} pontos"
        return pontuacao, feedback

    def is_finalizado(self):
        return self._finalizado