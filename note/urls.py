from django.urls import path
from note import views

urlpatterns = [
    path("intro/",views.intro,name="intro"),
    path("intro/home/",views.home,name="home"),

]