from django.test import TestCase
from django.utils import timezone

from .models import Course, Step


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python regular expressions",
            description="Some description"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTests(TestCase):
    def test_step_default(self):
        course = Course.objects.create(
            title="Python regular expressions",
            description="Some description"
        )
        step = Step.objects.create(
            title="Title",
            description="Desc",
            order=1,
            course=course,
        )
        self.assertEquals(step.content, '')
        self.assertEquals(step.order, 1)


class CoruseViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python testing',
            description='Learn to write tests in Pything')
        self.course2 = Course.objects.create(
            title='New Course',
            description='A new course')
        self.step = Step.objects.create(
            title='Intro to Doctests',
            description='Learn to write tests in the docstring',
            course=self.course)
