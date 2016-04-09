from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.models import Article
from api.serializers import UserSerializer, ArticleSerializer

# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
