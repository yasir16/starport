from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    # ex: /courses/
    path("", views.index, name="index"),
    # ex: /courses/1
    path("<int:cs_id>/", views.cs_detail, name="cs_detail"),
    # ex: /courses/1/1
    path("<int:cs_id>/<int:c_id>", views.c_detail, name="c_detail"),
    # ex: /courses/add
    path("add", views.add_to_queue, name="add_to_queue")
]

