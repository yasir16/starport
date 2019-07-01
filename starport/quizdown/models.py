from django.utils.translation import ugettext_lazy as _
from django.db import models
from courses.models import CourseSet
from userprofile.models import UserProfile


class QuestionSet(models.Model):
    cs = models.OneToOneField(CourseSet, on_delete=models.CASCADE)
    passingscore = models.PositiveSmallIntegerField("passing score", default=1)
    maxscore = models.PositiveSmallIntegerField("max score", default=1)
    maxattempt = models.PositiveSmallIntegerField("max attempt", default=1)
    updated_on = models.DateTimeField("last updated", auto_now=True)


class UserQuizSubmission(models.Model):
    questionset = models.ForeignKey(QuestionSet, on_delete=models.SET_NULL, null=True)
    userprofile = models.ForeignKey(
        UserProfile, related_name="submitted_by", on_delete=models.CASCADE
    )
    last_submission_on = models.DateTimeField("last updated", auto_now=True)
    usermaxscore = models.PositiveSmallIntegerField("user max score", default=0)
    userattempt = models.PositiveSmallIntegerField("user attempt", default=0)

    def save(self, *args, **kwargs):

        if self.passingscore > self.maxscore:
            raise ValueError("passingscore can't be greater than maxscore")

        super().save(*args, **kwargs)

    class Meta:
        unique_together = [("questionset", "userprofile")]
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Question(models.Model):
    questionset = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    prompt = models.TextField("question prompt", max_length=1000, blank=False)
    questionscore = models.PositiveSmallIntegerField("question score", default=1)
    questionorder = models.PositiveSmallIntegerField("question order")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(
        max_length=1000, blank=False, help_text=_("Pick this choice?")
    )
    correct = models.BooleanField(
        blank=False, default=False, help_text=_("Is this the right answer?")
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
