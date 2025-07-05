import logging
import requests
logger = logging.getLogger(__name__)

class DeepSeekClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/"

    def generate_response(self, prompt, model="deepseek-chat", max_tokens=150):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": "Você é um especialista em Django ORM."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }

        logger.debug(f"Enviando requisição para {self.base_url}chat/completions")
        logger.debug(f"Cabeçalhos: {headers}")
        logger.debug(f"Corpo da requisição: {data}")
        response = requests.post(f"{self.base_url}chat/completions", headers=headers, json=data)
        logger.debug(f"Resposta da API: {response.status_code} - {response.text}")
        response.raise_for_status()
        return response.json()