from django.urls import path
from .views import mensagem_api

urlpatterns = [
    path('mensagens/', mensagem_api, name='mensagens_api'),
]
