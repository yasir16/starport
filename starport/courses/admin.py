from django.contrib import admin

# Register your models here.
from .models import CourseSet, Course, ApprovalQueue

admin.site.register([CourseSet, Course, ApprovalQueue])