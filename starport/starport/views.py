from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Welcome to Starport</h2>')

