from django.urls import path
from .views import CreateEmployeeAPIView,VoteAPIView

urlpatterns = [
 path('create_employee/',
      CreateEmployeeAPIView.as_view(),
      name="create-employee"),
 path('vote/',
      VoteAPIView.as_view(),
      name="vote"),
 
]
