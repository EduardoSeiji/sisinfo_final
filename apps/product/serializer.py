from rest_framework import serializers
from .models import Product

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('category','seller','title','slug','description','price','date_added','image','thumbnail')
