from django.contrib import admin
from .models import User, Employer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_staff', 'is_superuser']
    search_fields = ['email']
    ordering = ['id']

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'contact_person_name', 'user', 'created_at']
    search_fields = ['company_name', 'contact_person_name']
    ordering = ['-created_at']
