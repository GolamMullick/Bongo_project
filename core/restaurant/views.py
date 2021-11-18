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
from .models import Restaurant,Menu
from users.permissions import IsAdmin, IsRestaurant
from django.conf import settings
from django.db.models import Q
from .serializers import UploadMenuSerializer,MenuListSerializer

class CreateRestaurant(APIView):
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
            
        new_restaurant=Restaurant(name=name,address=address,contact_no=contact_no,user=request.user.username)
        new_restaurant.save()
        
        response_data = {
              "msg": "Restaurant Created",
              "name":new_restaurant.name,
              "contact_no":new_restaurant.contact_no,
              "adress":new_restaurant.address
              
        }
       
        return Response({'status':'success', 'data':response_data},status=HTTP_400_BAD_REQUEST )
        
        
class UploadMenu(APIView):
    permission_classes = [IsRestaurant]

    def post(self, request,format=None):

        try:
            req = request.data
            todays_date = settings.CURRENT_DATE.date()
            print('today_date',todays_date)
            menu = Menu.objects.filter(
                Q(restaurant__id=int(req.get('restaurant')))
                and Q(created_at__date=todays_date))

            if menu.exists():
                response_data = {
                    "msg": "Menu already added.",
                    "data": None}
                return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )

            serializer = UploadMenuSerializer(data=req)

            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "msg": "Menu uploaded",
                    "data": serializer.data}
                return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )

        except Exception as e:
            print('error',e)
            response_data = {"msg": "Unexpected error occured", "success": False, "data": None}
            return Response({'status':'success', 'data':response_data},status=HTTP_400_BAD_REQUEST )
        
class CurrentDayMenuList(APIView):
    permission_classes = [IsRestaurant]
    
    def get(self, request):
        todays_date = settings.CURRENT_DATE.date()
        qs = Menu.objects.filter(Q(created_at__date=todays_date))
        serializer = MenuListSerializer(qs, many=True)
        response_data = {"msg": 'success', "data": serializer.data, "success": True}
        return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )
        
        