from rest_framework import serializers

class CryptoPriceSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    date = serializers.DateField(format="%Y-%m-%d")
