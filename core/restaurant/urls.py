from django.urls import path
from .views import CreateRestaurant,UploadMenu,CurrentDayMenuList

urlpatterns = [
 path('create_restaurant/',
      CreateRestaurant.as_view(),
      name="create-restaurant"),
  path('upload_menu/',
      UploadMenu.as_view(),
      name="upload-menu"),
   path('current_day_menu/',
      CurrentDayMenuList.as_view(),
      name="current-menu"),
  
]
