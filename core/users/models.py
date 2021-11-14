from django.conf import settings
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    USER_TYPES = (
       ("superadmin", "superadmin"),
       ("admin", "admin"),
       ("employee","employee"),
       ("restaurant","restaurant")
 
    )
    USER_TYPES_MAP = dict(USER_TYPES)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100,default=None, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=True)
    mobile_no = models.CharField(null=True, blank=True, max_length=16)
    user_type = models.CharField(choices=USER_TYPES,max_length=28)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','user_type']
    
    def __str__(self):
        return self.username
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL) 
def create_auth_token(sender,instance=None,created=False, **kwargs):
    
    if created:
        Token.objects.create(user=instance)
        
    
    
        
    
    