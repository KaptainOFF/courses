from django.shortcuts import render
from courses.models import Course
# Create your views here.
from django.http import HttpResponse


def courses(request):
    all_courses = Course.objects.all()
    output = ', '.join([str(course) for course in all_courses])
    return HttpResponse(output)
