from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inotech", views.home, name="inotech"),
    path("<int:id>/", views.sobre, name="sobre"),
    path("teacher/", views.teacher, name="teacher"),
    path("student/", views.student, name="student"),

]