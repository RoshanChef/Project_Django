from django.contrib import admin
from .models import register , author , feedback

from import_export.admin import ImportExportModelAdmin
from import_export import resources


# class register_(admin.ModelAdmin):
class register_(ImportExportModelAdmin):
    list_display =['id','name', 'number', 'email', 'address','password']
    search_display = ['name']
    list_filter = ['name']

class author_(admin.ModelAdmin):
    list_display = ['id','name', 'post']

class feedback_(admin.ModelAdmin):
    list_display = ['id' , 'name', 'email', 'message']
    list_filter = ['email']

# Register your models here.

admin.site.register(register , register_)
admin.site.register(author , author_)
admin.site.register(feedback , feedback_)