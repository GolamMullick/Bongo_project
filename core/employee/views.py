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
from .models import Employee,Vote
from users.permissions import IsAdmin, IsEmployee
from django.db.models import Q
from django.conf import settings
from restaurant.models import Menu, Restaurant
from .serializers import ResultMenuListSerializer

class CreateEmployeeAPIView(APIView):
    permission_classes = [IsAdmin]
    
    def post(self, request, format=None):
        
        name = request.data.get('name')
        employee_no =request.data.get ('employee_no')
        
        if name is None or employee_no is None:
            return Response({'error': 'Please provide both name and employee number'},
                    status=HTTP_400_BAD_REQUEST)
            
        employee_data = Employee.objects.filter(Q(name=name) and Q(employee_no=employee_no))
        
        if employee_data.exists():
            return Response({'error': 'Please create new employee, this employee is already created'},
                    status=HTTP_400_BAD_REQUEST)
            
        new_employee=Employee(name=name,employee_no=employee_no)
        new_employee.save()
        
        response_data = {
              "msg": "Employee Created",
              "name":new_employee.name,
              "employee_no":new_employee.employee_no
              
        }
       
        return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )
        
        
class VoteAPIView(APIView):
    permission_classes = [IsEmployee]

    def get(self, request, menu_id):
        username = request.get('username')
        todays_date = settings.CURRENT_DATE.date()

        employee = Employee.objects.get(user__username=username)
        menu = Menu.objects.get(id=menu_id)

        if Vote.objects.filter(
                employee__user__username=username,
                voted_at__date=todays_date,
                menu__id=menu_id).exists():
            response_data = {"msg": 'You already voted!', "data": None}
            
            return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )
       
        else:
            new_vote = Vote.objects.create(
                employee=employee,
                menu=menu

            )
            menu.votes += 1
            menu.save()

            qs = Menu.objects.filter(Q(created_at__date=todays_date))
            serializer = ResultMenuListSerializer(qs, many=True)
            response_data = {
                "msg": 'You voted successfully!',
                "data": serializer.data,
            }
            
            return Response({'status':'success', 'data':response_data},status=HTTP_200_OK )
