from .models import Restaurant, Menu
from rest_framework.serializers import ModelSerializer

class  CreateRestaurantSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = Restaurant
        fields = ('name','contact_no','address')

class UploadMenuSerializer(ModelSerializer):
    
    def create(self, validated_data):

        menu = Menu(
            file=validated_data['file'],
            restaurant=validated_data['restaurant'],
            uploaded_by=validated_data['uploaded_by']
        )
        menu.save()
        return menu

    class Meta:
        model = Menu
        
        fields = [
            'restaurant',
            'file',
            'uploaded_by',
            'name'
        ]
        
class MenuListSerializer(ModelSerializer):
    
    class Meta:
        model = Menu
        fields = '__all__'
        
        

