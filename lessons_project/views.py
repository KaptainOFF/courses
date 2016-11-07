from django.http import HttpResponse


def hello_python(request):
    return HttpResponse("Hello World")

