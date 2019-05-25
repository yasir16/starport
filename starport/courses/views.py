from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError

from .models import CourseSet, ApprovalQueue
from .forms import AddtoQueueForm

# Create your views here.
def index(request):
    coursesets = CourseSet.objects.order_by("-updated_on")[:5]
    add_form = AddtoQueueForm()
    template = loader.get_template("courses/index.html")
    context = {"coursesets": coursesets, "add_form": add_form}

    return HttpResponse(template.render(context, request))


def cs_detail(request, cs_id):
    try:
        courseset = CourseSet.objects.get(pk=cs_id)
    except CourseSet.DoesNotExist:
        raise Http404("The Course you're looking for is not found")
    template = loader.get_template("courses/courseset.html")
    context = {"courseset": courseset}
    return HttpResponse(template.render(context, request))


def c_detail(request, cs_id, c_id):
    return HttpResponse(f"The detail page for Course {c_id}")


def add_to_queue(request):
    form = AddtoQueueForm(request.POST)
    if form.is_valid():
        existing_q = ApprovalQueue.objects.filter(repo_url=request.POST["repo_url"])
        if existing_q:
            return HttpResponse(
                "Fail: This repo has already been submitted in the past."
            )
        else:
            ApprovalQueue(repo_url=request.POST["repo_url"]).save()
            return HttpResponseRedirect(reverse("courses:index"))
    else:
        print(form.errors)
        template = loader.get_template("courses/index.html")
        coursesets = CourseSet.objects.order_by("-updated_on")[:5]
        add_form = AddtoQueueForm()
        context = {
            "coursesets": coursesets,
            "add_form": add_form,
            "error_message": form.errors,
        }
        return HttpResponse(template.render(context, request))
