import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ApprovalQueue(models.Model):
    repo_url = models.SlugField("repo slug", unique=True)
    submitted_on = models.DateTimeField("submitted on", auto_now_add=True)
    submitted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="discovered"
    )
    approved_status = models.BooleanField("approved status", default=False)
    approved_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = [
            (
                "approve_course",
                "Can approve a course submitted to the Queue by setting status as True",
            ),
            (
                "remove_course",
                "Can remove a course from the Queue by setting status as False",
            ),
        ]

        ordering = ["-submitted_on", "submitted_by"]

        def __str__(self):
            return self.repo_url


class CourseSet(models.Model):
    repo_url = models.SlugField("repo slug", unique=True)
    created_on = models.DateTimeField("created on", auto_now_add=True)
    updated_on = models.DateTimeField("last updated", auto_now=True)
    approved_by = models.OneToOneField(
        ApprovalQueue, on_delete=models.SET_NULL, null=True
    )
    owner = models.SlugField("owner")
    title = models.CharField("title", max_length=40)
    description = models.TextField(
        "description", max_length=300, default="No description yet"
    )
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
    description = models.TextField(
        "description", max_length=300, default="No description yet"
    )
    star_n = models.PositiveIntegerField(default=0)
    course_url = models.URLField("course url")

    def __str__(self):
        return self.course_url
