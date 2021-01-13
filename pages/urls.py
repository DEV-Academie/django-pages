from django.urls import path
from pages.views import hello, homepage

urlpatterns = [
    path("", homepage, name="home"),
    path("hello/", hello, name="hello"),
]
