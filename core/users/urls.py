
from django.urls import path
from . import views

urlpatterns = [
    path('users_register/', views.UserDetails.as_view(), name='users'),
    path('login/', views.login, name='account-auth-token'),
    path('logout/', views.logout, name='account-auth-logout'),
]


