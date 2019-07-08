import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ApprovalQueue, CourseSet
from .parser import ExtractChoices #import error idk why


def createCourse(course_directory):
    pass


def course_n_counter(repo_url):
    import re

    req = requests.get("https://api.github.com/repos/" + repo_url + "/contents")
    json = req.json()
    reg = re.compile("^[\d]+[._-][\w]+$")
    course_directory = [
        j["name"] for j in json if j["type"] == "dir" and reg.match(j["name"])
    ]
    return len(course_directory)


def createCourseSet(repo_url, approved_by):
    import mistune

    req = requests.get("https://api.github.com/repos/" + repo_url)
    json = req.json()
    quizurl = requests.get(
        f"https://raw.githubusercontent.com/{repo_url}/master/quiz.md"
    )
    quizcontent = quizurl.content.decode("utf-8")

    if "id" in json:
        created_on = json["created_at"]
        updated_on = json["updated_at"]
        owner = json["owner"]["login"]
        title = json["name"]
        description = json["description"]
        star_n = json["stargazers_count"]
        course_n = course_n_counter(repo_url)
        CourseSet(
            repo_url=repo_url,
            created_on=created_on,
            updated_on=updated_on,
            approved_by=approved_by,
            owner=owner,
            title=title,
            description=description,
            star_n=star_n,
            course_n=course_n_counter(repo_url),
            quizcontent=mistune.markdown(quizcontent),
        ).save()


def createQuiz(repo_url):
    """
    Create quiz from CourseSet.objects model
    """
    CourseSet.quizcontent()
    ExtractChoices()
    pass


@receiver(post_save, sender=ApprovalQueue)
def cs_approved_signal(sender, instance, **kwargs):
    print(f"Course Set {instance.repo_url} is added and pending approval.")
    if instance.approved_status:
        print(
            f"Course Set {instance.repo_url} has been approved. Github API running..."
        )
        createCourseSet(instance.repo_url, approved_by=instance)
        print("Added CourseSet to the platform.")


# def cs_approved_signal(sender, instance, **kwargs):
#     print("A course set has been approved. Github API running...")
#     post_save.connect(cs_approved_signal, sender=ApprovalQueue)
