from django.urls import path
from pages.views import Hello, HelloSub, HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("hello/", Hello.as_view(), name="hello"),
    path("hello/sub/", HelloSub.as_view(), name="sub"),
]
