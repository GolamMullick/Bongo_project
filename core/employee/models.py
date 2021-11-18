from django.db import models
from users.models import User
from restaurant.models import Menu

class Employee(models.Model):
    """Represents user class model"""
    employee_no = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default=None,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
    
class Vote(models.Model):
    """Represents vote class model"""
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee}'