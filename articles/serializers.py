from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'contents',]

    