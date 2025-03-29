# API Middleware Binance

## 📌 Sobre o Projeto

Essa API serve como um middleware para buscar o preço histórico de criptomoedas na Binance. Ela recebe uma moeda e uma data e retorna o preço de fechamento daquele dia.

## 🚀 Tecnologias Utilizadas

- **Python** (Django REST Framework)
- **Docker**
- **Binance API**

## 🛠 Como Rodar o Projeto

### 🐳 Rode o Docker

1. Clone o repositório:
   ```sh
   git clone https://github.com/Gabriel-dev001/Api-Middleware-Binance.git
   cd Api-Middleware-Binance
   ```

2. Construa a imagem Docker:
   ```sh
   docker build -t api-middleware-binance .
   ```
3. Execute o container:
   ```sh
   docker run -p 8000:8000 api-middleware-binance
   ```

## 📡 Como Usar a API

### 🔍 Endpoint para obter o preço histórico:

**Rota:**
```
PUT /historical-price/
```

**Exemplo de Requisição:**
```json
{
    "symbol": "BTC",
    "date": "2024-02-01"
}
```

**Exemplo de Resposta:**
```json
{
    "symbol": "BTC",
    "date": "2024-02-01",
    "price": "42500.50"
}
```

# 📞 CONTATO  

👨‍💻 **Desenvolvedor:** **Gabriel**

