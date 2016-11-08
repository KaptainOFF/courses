from django.shortcuts import render
from courses.models import Course


def course_list(request):
    all_courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses' : all_courses})
