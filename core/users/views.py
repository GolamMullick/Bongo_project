from django.contrib.auth import authenticate
from django.contrib.auth import login as session_login
from django.contrib.auth import logout as session_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)

import string
import random
from .models import User
from rest_framework.response import Response
from .permissions import IsAdmin

def generate_password_by_policy(length=8):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    special = '!#$%&():;<=>?@[]^{|}~'
    number = string.digits
    password = []
    password.extend([random.choice(upper_case) for i in range(2)])
    password.extend([random.choice(lower_case) for i in range(2)])
    password.extend([random.choice(special) for i in range(2)])
    password.extend([random.choice(number) for i in range(2)])

    random.shuffle(password)
    password = ''.join(password)
    return password
    
class UserDetails(APIView):
    permission_classes = [IsAdmin]
    def post(self,request, format=None):
        name = request.data.get('username')
        email = request.data.get('email')
        mobile_no = request.data.get('mobile_no')
        user_type = request.data.get('user_type')



        if name is None:
            return Response({'error':'Please provide username'}, status=HTTP_400_BAD_REQUEST)

        if mobile_no is None or not mobile_no.startswith('01') or len(mobile_no) != 11:
                return Response({'error':'You need to provide a valid Bangladeshi mobile number without country code.'}, status=HTTP_400_BAD_REQUEST)
    
        if email is None or user_type is None:
            return Response({'error': 'Email or user type can not be null.'}, status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=HTTP_400_BAD_REQUEST)
     

        if (user_type != User.USER_TYPES_MAP['employee']) and (user_type != User.USER_TYPES_MAP['restaurant']):
            return Response({'error': 'You must specify correct user type.'}, status=HTTP_404_NOT_FOUND)


        middle_name = f'_{user_type}_'

        username =  middle_name + email

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=HTTP_400_BAD_REQUEST)

        password = generate_password_by_policy()
        new_user = User(name=name,username=username,email=email,mobile_no=mobile_no,user_type=user_type)
        new_user.set_password(password)
        new_user.save()
        return Response({'username': new_user.username, 'user_type': new_user.user_type,'email' : new_user.email, 'password': password}, status=HTTP_200_OK)
