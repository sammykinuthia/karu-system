from hashlib import new
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from blog.models import News

def index(request):
    news = ContentType.objects.get_for_model(News)
    print("news:",news.get_all_objects_for_this_type())
    return render(request,"academic/index.html")

