from django.urls import path,include
from . import views
urlpatterns = [
    #path("", "demo/index.html",name="index"),
    path("", views.index,name="index"),

    
]