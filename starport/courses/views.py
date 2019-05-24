from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError

from .models import CourseSet, ApprovalQueue
from .forms import AddtoQueueForm

# Create your views here.
def index(request):
    coursesets = CourseSet.objects.order_by('-updated_on')[:5]
    add_form = AddtoQueueForm()
    template = loader.get_template('courses/index.html')
    context = {
        'coursesets': coursesets,
        'add_form': add_form
    }


    return HttpResponse(template.render(context, request))

def cs_detail(request, cs_id):
    try:
        courseset = CourseSet.objects.get(pk=cs_id)
    except CourseSet.DoesNotExist:
        raise Http404("The Course you're looking for is not found")
    template = loader.get_template('courses/courseset.html')
    context = {
        'courseset': courseset,
    }
    return HttpResponse(template.render(context, request))

def c_detail(request, cs_id, c_id):
    return HttpResponse(f'The detail page for Course {c_id}')

def add_to_queue(request):
    try:
        aq = ApprovalQueue(repo_url=request.POST['repo_url'])
        aq.save()
    except:
        raise HttpResponse("Fail: This repo has already been submitted in the past.")
    else:
        return HttpResponseRedirect(reverse('courses:index'))