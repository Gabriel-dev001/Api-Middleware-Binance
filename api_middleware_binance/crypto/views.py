from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def mensagem_api(request):
    """
    Retorna uma lista de mensagens de teste.
    """
    mensagens = [
        {"texto": "Gabriel aLindo"},
        {"id": 2, "texto": "API Django funcionando!"},
    ]
    return Response(mensagens)

