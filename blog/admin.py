from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdminApp(admin.ModelAdmin):
    list_display = ('title','published_on', 'last_modified')