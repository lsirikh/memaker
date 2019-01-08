from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'route',
                    'agree',
                    'email_confirmed',
                    'gender',
                    'birth',
                    'address',
                    'phone',
                    'route',
                    ]