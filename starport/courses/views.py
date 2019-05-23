from django.http import HttpResponse, Http404
from django.template import loader

from .models import CourseSet

# Create your views here.
def index(request):
    coursesets = CourseSet.objects.order_by('-updated_on')[:5]
    template = loader.get_template('courses/index.html')
    context = {
        'coursesets': coursesets,
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
