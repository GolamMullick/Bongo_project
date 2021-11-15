from django.contrib.auth import authenticate
from django.contrib.auth import login as session_login
from django.contrib.auth import logout as session_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)
import string
import random
from rest_framework.response import Response
from .models import Restaurant
from users.permissions import IsAdmin

class CreateRestaurantAPIView(APIView):
    permission_classes = [IsAdmin]
    
    def post(self, request, format=None):
        
        name = request.data.get('name')
        address = request.data.get('address')
        contact_no =request.data.get ('contact_no')
        
        if name is None or address is None or contact_no is None:
            return Response({'error': 'Please provide name, address and contact number'},
                    status=HTTP_400_BAD_REQUEST)
            
        restaurant = Restaurant.objects.filter(name=name)
        
        if restaurant.exists():
            return Response({'error': 'Please create new restaurant, this restaurant is already created'},
                    status=HTTP_400_BAD_REQUEST)
            
        new_restaurant=Restaurant(name=name,address=address,contact_no=contact_no)
        new_restaurant.save()
        
        response_data = {
              "msg": "Restaurant Created",
              "name":new_restaurant.name,
              "contact_no":new_restaurant.contact_no,
              "adress":new_restaurant.address
              
        }
       
        return Response({'status':'success', 'data':response_data},status=HTTP_400_BAD_REQUEST )
        
        
