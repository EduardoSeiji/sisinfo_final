from rest_framework import serializers
from .models import Product

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('first_name','last_name','email','address','zipcode','place','phone','created_at','paid_amount','sellers','')
