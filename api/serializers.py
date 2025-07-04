from rest_framework import serializers
from app.models import Product, User

class SerializersProductAPI(serializers.ModelSerializer):
    tablePromotion = serializers.CharField()
    promotion = serializers.BooleanField()
    category = serializers.StringRelatedField(
        source = 'category.name',
        read_only = True
    )
    subCategory = serializers.PrimaryKeyRelatedField(
        # queryset = Product.objects.all(),
        many = True,
        source = 'category.subCategory',
        read_only = True
    )
    
    class Meta:
        model = Product
        fields = ["id", "author", "title", 
                  "slug", "price", "description", 
                  "textAdd", "avaliacoes", "tablePromotion", 
                  "promotion", "category", "subCategory",
                  "urlProduct"
        ]
    
    # def validate(self, attrs):
    #     print("Validate Method")
    #     return super().validate(attrs)
    
    # def validate_title(self, value):
    #     print("Validate Title", value)
    #     return value
    
class SerializerCreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]