from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import get_historical_price

@api_view(["PUT"])
def get_crypto_price(request):
    """
    Recebe um JSON com `symbol` e `date`, consulta a Binance e retorna o preço.
    Exemplo de corpo da requisição:
    {
        "symbol": "BTC",
        "date": "2024-02-01"
    }
    """
    try:
        data = request.data
        symbol = data.get("symbol")
        date = data.get("date")

        if not symbol or not date:
            return Response({"error": "Campos 'symbol' e 'date' são obrigatórios"}, status=400)

        result = get_historical_price(symbol, date) 
        return Response(result)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
