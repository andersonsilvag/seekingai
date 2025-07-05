from django.urls import path
from .views import AskOpenAiViewSet,AskDeepSeekViewSet

app_name = 'gpt'  # Define o nome do aplicativo
urlpatterns = [
    path('ask-openai/', AskOpenAiViewSet.as_view({'post': 'create'}), name='openai_ask_view'),
    path('ask-deepseek/', AskDeepSeekViewSet.as_view({'post': 'create'}), name='deepseek_ask_view'),
]