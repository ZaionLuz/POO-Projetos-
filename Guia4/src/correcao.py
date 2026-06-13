from typing import List, Tuple, Dict

from .perguntadiscursiva import PerguntaDiscursiva
from .llmservice import LLMService


class Correcao:

    @staticmethod
    def corrigir_discursiva(
        pergunta: PerguntaDiscursiva,
        resposta_aluno: str,
        service: LLMService = None
    ) -> Dict:

        if service is None:
            service = LLMService()

        return service.corrigir_resposta(pergunta, resposta_aluno)

    @staticmethod
    def criar_prompt_correcao(
        pergunta: PerguntaDiscursiva,
        resposta_aluno: str
    ) -> str:

        return (
            f"Pergunta: {pergunta.texto} | "
            f"Esperado: {pergunta.resposta_esperada} | "
            f"Aluno: {resposta_aluno}"
        )