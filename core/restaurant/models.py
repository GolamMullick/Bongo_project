from django.db import models
from users.models import User
# Create your models here.

class Restaurant(models.Model):
    """Represents restaurant class model"""
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    contact_no = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Menu(models.Model):
    """Represents menu class model"""
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    file = models.FileField(upload_to='menus/% Y/% m/% d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.CharField(max_length=50, null=True, blank=True)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.restaurant.name