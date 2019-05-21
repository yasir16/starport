from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello visitor. You're at the course management index.")
