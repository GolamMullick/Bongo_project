
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User
from django.contrib.auth.models import Group

class MyUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        # Get form from original UserAdmin.
        form = super(MyUserAdmin, self).get_form(request, obj, **kwargs)
        # if 'user_permissions' in form.base_fields:
        #     permissions = form.base_fields['user_permissions']
        #     permissions.queryset = permissions.queryset.filter(content_type__name='log entry')
        return form

admin.site.register(User, MyUserAdmin)


