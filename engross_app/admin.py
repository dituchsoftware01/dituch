from django.contrib import admin
from.models import UserFormData
# Register your models here.

class UserFormDataModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender', 'mobile', 'batch', 'qualification']

# Register the UserFormData model with the UserFormDataModelAdmin options
admin.site.register(UserFormData, UserFormDataModelAdmin)
