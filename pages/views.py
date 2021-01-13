from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, Class!")
