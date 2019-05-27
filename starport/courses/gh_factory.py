import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ApprovalQueue, CourseSet

def createCourseSet(repo_url, approved_by):
    req = requests.get("https://api.github.com/repos/" + repo_url)   
    json = req.json()
    if "id" in json:
        created_on = json["created_at"]
        updated_on = json["updated_at"]
        owner = json["owner"]["login"]
        title = json["name"]
        description = json['description'] 
        star_n = json["stargazers_count"]
        # TODO: add image and course_n attributes as definition, 
        # course_n should be updated using post_update Signals
        CourseSet(repo_url=repo_url, 
                created_on=created_on,
                updated_on=updated_on,
                approved_by=approved_by,
                owner=owner,
                title=title,
                description=description,
                star_n=star_n
                ).save()


# TODO: connect when approved to add to CourseSet 
@receiver(post_save, sender=ApprovalQueue)
def cs_approved_signal(sender, instance, **kwargs):
    print("A course set has been approved. Github API running...")
    createCourseSet('onlyphantom/sqlalchemy-tutorial', 
    approved_by=instance)
    print("Added CourseSet to the platform.")

# def cs_approved_signal(sender, instance, **kwargs):
#     print("A course set has been approved. Github API running...")
#     post_save.connect(cs_approved_signal, sender=ApprovalQueue)
