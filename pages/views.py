from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "pages/home.html"


class Hello(TemplateView):
    template_name = "pages/hello.html"
