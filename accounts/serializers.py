from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model

class UserSerializer(ModelSerializer):
    username = CharField(max_length=100)


    class Meta:
        model = get_user_model()
        fields = ['id', 'username']