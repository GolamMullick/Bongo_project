from restaurant.models import Menu
from rest_framework.serializers import ModelSerializer


class ResultMenuListSerializer(ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'id',
            'file',
            'restaurant',
            'votes',
            'created_at'
        ]