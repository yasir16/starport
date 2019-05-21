import datetime
from django.db import models
from django.utils import timezone


class CourseSet(models.Model):
    repo_url = models.URLField("repo url")
    created_on = models.DateTimeField("created on")
    updated_on = models.DateTimeField("last updated")
    owner = models.SlugField("owner")
    favorite_n = models.IntegerField(default=0)
    # TODO: reference to User model for owner?

    def __str__(self):
        return self.repo_url

    def updated_recently(self):
        return self.updated_on >= timezone.now() - datetime.timedelta(days=7)


class Course(models.Model):
    courseset = models.ForeignKey(CourseSet, on_delete=models.CASCADE)
    created_on = models.DateTimeField("created on")
    last_updated = models.DateTimeField("last updated")
    favorite_n = models.IntegerField(default=0)
    comments_n = models.IntegerField(default=0)
    course_url = models.URLField("course url")

    def __str__(self):
        return self.course_url