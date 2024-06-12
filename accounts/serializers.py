from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class UserSerializer(ModelSerializer):
    username = CharField(max_length=100)
    password = CharField(write_only=True, required=True, validators=[validate_password])


    def create(self, validated_data):
        user_model = get_user_model()
        user = user_model.objects.create(
            username = validated_data['username'],
            # email = validated_data.get('email')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']