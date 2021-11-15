from .models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ('username', 'email', 'mobile_no', 'user_type')

