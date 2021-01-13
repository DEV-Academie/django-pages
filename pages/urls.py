from django.urls import path
from pages.views import Hello, HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("hello/", Hello.as_view(), name="hello"),
]
