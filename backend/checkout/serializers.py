from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_name(self, value):
            
            if len(value) > 1:
                raise serializers.ValidationError("Name must be a single character.")

            # duplicate name not consider
            if Product.objects.filter(name=value).exists():
                raise serializers.ValidationError("A product with this name already exists.")

            return value
