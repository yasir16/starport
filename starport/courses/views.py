from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import CourseSet, ApprovalQueue
from .forms import AddtoQueueForm
from quizdown.models import QuestionSet, Question, Choice


@login_required
def index(request):
    coursesets = CourseSet.objects.order_by("-updated_on")[:5]
    add_form = AddtoQueueForm()
    template = loader.get_template("courses/index.html")
    context = {"coursesets": coursesets, "add_form": add_form}

    return HttpResponse(template.render(context, request))


def cs_detail(request, cs_id):
    try:
        courseset = CourseSet.objects.get(pk=cs_id)
        questions = Question.objects.filter(questionset__cs=cs_id)
    except CourseSet.DoesNotExist:
        raise Http404("No project with that id.")
        # return render_to_response('custom_404_template.html')
    template = loader.get_template("courses/courseset.html")
    context = {"courseset": courseset, "questions": questions}
    return HttpResponse(template.render(context, request))


def c_detail(request, cs_id, c_id):
    return HttpResponse(f"The detail page for Course {c_id}")


@login_required
def participation(request):
    user = request.user
    coursesets = CourseSet.objects.filter(participated_by__user=user)
    template = loader.get_template("courses/participation.html")
    context = {"coursesets": coursesets}
    return HttpResponse(template.render(context, request))


def participate(request, cs_id):
    print(f"Participating {cs_id}")
    cs = get_object_or_404(CourseSet, pk=cs_id)
    template = loader.get_template("courses/courseset.html")
    context = {"courseset": cs}
    if "participate_btn" in request.POST:
        print(request.POST["participate_btn"])
        request.user.userprofile.participate.add(cs)
    else:
        request.user.userprofile.participate.remove(cs)
    return HttpResponse(template.render(context, request))


def add_to_queue(request):
    form = AddtoQueueForm(request.POST)
    if form.is_valid():
        repourl = request.POST["repo_url"].lower()
        existing_c = CourseSet.objects.filter(repo_url=repourl)
        if existing_c:
            return HttpResponse("Fail: This repo is already a course on Positif.io")
        existing_q = ApprovalQueue.objects.filter(repo_url=repourl)
        if existing_q:
            return HttpResponse(
                "Fail: This repo has already been submitted in the past."
            )
        else:
            ApprovalQueue(repo_url=repourl, submitted_by=request.user).save()
            return HttpResponseRedirect(reverse("courses:index"))
    else:
        template = loader.get_template("courses/index.html")
        coursesets = CourseSet.objects.order_by("-updated_on")[:5]
        add_form = AddtoQueueForm()
        context = {
            "coursesets": coursesets,
            "add_form": add_form,
            "error_message": form.errors,
        }
        return HttpResponse(template.render(context, request))


def approve_from_queue(request):
    if "approve_btn" in request.POST:
        repourl = request.POST["approve_btn"]
        print(f"{request.user} approved: {repourl}")
        approval_item = get_object_or_404(ApprovalQueue, repo_url=repourl)
        approval_item.approved_status = True
        approval_item.save(update_fields=["approved_status"])

    if "delete_btn" in request.POST:
        repourl = request.POST["delete_btn"]
        print(f"{request.user} deleted: {repourl}")
        approval_item = get_object_or_404(ApprovalQueue, repo_url=repourl)
        approval_item.delete()

    return HttpResponseRedirect(reverse("courses:approval-review"))


class ReviewList(ListView):
    model = ApprovalQueue
    template_name = "courses/approval.html"
    paginate = 10

    def get_queryset(self):
        return ApprovalQueue.objects.filter(approved_status=False)
