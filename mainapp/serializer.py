from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from . models import Article,Category

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
