import datetime
from django.db import models
from django.utils import timezone


class CourseSet(models.Model):
    repo_url = models.URLField("repo url")
    created_on = models.DateTimeField("created on", auto_now_add=True)
    updated_on = models.DateTimeField("last updated", auto_now=True)
    owner = models.SlugField("owner")
    title = models.CharField("title", max_length=40)
    description = models.TextField("description", max_length=300, default="No description yet")
    image = models.URLField("repo image", null=True)
    course_n = models.PositiveSmallIntegerField(default=0)
    star_n = models.PositiveIntegerField(default=0)
    # TODO: reference to User model for owner?

    def __str__(self):
        return self.repo_url

    def updated_recently(self):
        return self.updated_on >= timezone.now() - datetime.timedelta(days=7)


class Course(models.Model):
    courseset = models.ForeignKey(CourseSet, on_delete=models.CASCADE)
    created_on = models.DateTimeField("created on", auto_now_add=True)
    updated_on = models.DateTimeField("last updated", auto_now=True)
    title = models.CharField("title", max_length=40)
    description = models.TextField("description", max_length=300, default="No description yet")
    star_n = models.PositiveIntegerField(default=0)
    course_url = models.URLField("course url")

    def __str__(self):
        return self.course_url