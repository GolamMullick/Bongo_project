from .models import Restaurant
from rest_framework.serializers import ModelSerializer

class  CreateRestaurantSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = Restaurant
        fields = ('name','contact_no','address')

