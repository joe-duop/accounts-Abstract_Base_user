from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


# Register your models here.
class CustomUserAdmin(UserAdmin):
    """override the admin-template  to make the template become neat and match my customuser model"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    """override the adduser-template to accept pass1 and pass2 instead of the hash password"""
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    """content that will be displayed on the templates"""
    list_display = ('email', 'name', 'is_staff')
    #list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name')
    ordering = ('email',)
    #filter_horizontal = ('groups', 'user_permissions',)






admin.site.register(models.UserProfile, CustomUserAdmin)