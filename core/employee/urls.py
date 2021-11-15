from django.urls import path
from .views import CreateEmployeeAPIView

urlpatterns = [
 path('create_employee/',
      CreateEmployeeAPIView.as_view(),
      name="create-employee"),
]
