import os

from openai import OpenAI, OpenAIError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .DeepSeekClient import DeepSeekClient  # Importando a classe
from apps.gpt.mixins import BaseAskViewSet

openai_api_key = os.getenv('OPENAI_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
class AskOpenAiViewSet(BaseAskViewSet):
    def api_response(self,question):
        try:
            client = OpenAI(api_key=openai_api_key)
            response = client.chat.completions.create(  
                model="gpt-3.5-turbo",
                messages=[  # Estrutura correta para chat
                    {"role": "system", "content": "Você é um assistente útil."},
                    {"role": "user", "content": question}
                ],
                max_tokens=1000,
            )
            resposta = response.choices[0].message.content.strip()
            answer = resposta
        except OpenAIError as e:
            answer = f"Erro na API: {e}"
        # Exemplo de código para retornar uma resposta em JSON
        return answer

class AskDeepSeekViewSet(BaseAskViewSet):
    def api_response(self,question):
        prompt = f"""
        Você é um assistente útil. O usuário relata:
        "{question}"
        """
       
        deepseek_client = DeepSeekClient(api_key=deepseek_api_key)
        response = deepseek_client.generate_response(prompt)
        answer = response["choices"][0]["message"]["content"].strip()
        # Exemplo de código para retornar uma resposta em JSON
        return answer

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'principal/index.html'
    login_url = '/accounts/login/'  # ou a URL que estiver usando no seu projeto

class DeepseekChatView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/deepseek/index.html'
    login_url = '/accounts/login/'  # ou a URL que estiver usando no seu projeto

class OpenIAChatView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/openai/index.html'
    login_url = '/accounts/login/'  # ou a URL que estiver usando no seu projeto
