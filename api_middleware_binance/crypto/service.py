import requests
from datetime import datetime

def get_historical_price(symbol, date):
    """Consulta o preço de fechamento da criptomoeda na data informada na API da Binance."""
    
    try:
        dt_object = datetime.strptime(date, "%Y-%m-%d")
        timestamp = int(dt_object.timestamp()) * 1000  

        # Construir a URL da API da Binance
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol.upper()}USDT&interval=1d&startTime={timestamp}&limit=1"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        if not data:
            return {"error": "Nenhum dado encontrado para a data informada"}

        return {
            "symbol": symbol.upper(),
            "date": date,
            "price": data[0][4] 
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Erro na requisição à Binance: {str(e)}"}

    except ValueError:
        return {"error": "Formato de data inválido. Use YYYY-MM-DD"}

    except Exception as e:
        return {"error": f"Erro interno: {str(e)}"}
