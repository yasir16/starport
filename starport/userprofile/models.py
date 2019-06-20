from django.db import models
from courses.models import CourseSet
from django.contrib.auth.models import User

# class Favorite(models.Model):
#     user = models.ForeignKey(User, unique=False)
#     post = models.ForeignKey(CourseSet, unique=False)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    participate = models.ManyToManyField(CourseSet, related_name='participated_by')

    def __str__(self):
            return self.user.username