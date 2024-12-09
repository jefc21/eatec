from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="index"),
    path("register", views.register, name="register"),
    path("main/", views.main, name="main"),
    path("student/", views.student, name="student"),
    path("student/<int:id>/", views.student_edit, name="student_edit"),
    path("inotech", views.home, name="inotech"),
    path("<int:id>/", views.sobre, name="sobre"),
    path("teacher/", views.teacher, name="teacher"),

]