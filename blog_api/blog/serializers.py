from .models import Category,Article
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'



