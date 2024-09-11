from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Article.objects.all().order_by('-pk')

    