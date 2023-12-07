from rest_framework import serializers
from .models import Product

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('name','destino_url','descricao','coordenadas','preco','categoria','empresaid')
