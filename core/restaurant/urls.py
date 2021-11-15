from django.urls import path
from .views import CreateRestaurantAPIView,UploadMenuAPIView

urlpatterns = [
 path('create_restaurant/',
      CreateRestaurantAPIView.as_view(),
      name="create-restaurant"),
  path('upload_menu/',
      UploadMenuAPIView.as_view(),
      name="upload-menu"),
]
