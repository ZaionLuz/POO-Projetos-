from typing import List, Tuple, Dict

import os
import json
from typing import Dict
from groq import Groq
from .perguntadiscursiva import PerguntaDiscursiva


class LLMService:
    def _init_(self, api_key: str = None, model: str = "llama3-70b-8192"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

        if model == "llama3-70b-8192":
            self.model = "llama-3.3-70b-versatile"
        else:
            self.model = model

        self.base_url = "https://api.groq.com"

        self.client = Groq(api_key=self.api_key) if self.api_key else None

    def corrigir_resposta(self, pergunta: PerguntaDiscursiva, resposta_aluno: str) -> Dict:
        prompt = f"""
Você é um professor avaliador rigoroso.

Pergunta: {pergunta.texto}
Resposta Esperada: {pergunta.resposta_esperada}
Resposta do Aluno: {resposta_aluno}

Responda APENAS JSON:
{{
    "correta": true,
    "pontuacao": 0.0,
    "feedback": "",
    "explicacao": ""
}}
"""

        try:
            resposta_texto = self._fazer_chamada_api(prompt)
            return json.loads(resposta_texto)

        except Exception as e:
            return self._tratar_erro(e, pergunta, resposta_aluno)

    def _fazer_chamada_api(self, prompt: str) -> str:
        if not self.client:
            raise ValueError("API Key do Groq não configurada.")

        chat_completion = self.client.chat.completions.create(
            model=self.model,
            temperature=0.1,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "Você responde apenas JSON válido."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return chat_completion.choices[0].message.content

    def _tratar_erro(self, e: Exception, pergunta: PerguntaDiscursiva, resposta_aluno: str) -> Dict:
        print(f"[LLMService Error]: {e}")

        resposta_esperada = pergunta.resposta_esperada or ""

        eh_correto = (
            str(resposta_aluno).strip().lower()
            == str(resposta_esperada).strip().lower()
        )

        return {
            "correta": eh_correto,
            "pontuacao": 1.0 if eh_correto else 0.0,
            "feedback": f"Fallback (erro API): {str(e)}",
            "explicacao": pergunta.get_explicacao() or "Sem explicação"
        }