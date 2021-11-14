
from django.urls import path

from . import views


urlpatterns = [
    path('users_register/', views.UserDetails.as_view(), name='users')
]