from django.contrib import admin
from api.models import UserVault

# Register your models here.
@admin.register(UserVault)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password'] 