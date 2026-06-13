from typing import List, Tuple, Dict

from .tentativaquestionario import TentativaQuestionario

class Questionario:
    def __init__(self, titulo: str, perguntas=None):
        self.titulo = titulo
        self.perguntas = perguntas if perguntas else []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def criar_attempt(self, usuario: str):
        return TentativaQuestionario(self, usuario)
