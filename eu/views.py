from django.http import HttpResponse
from .models import Student, Teacher
from django.template import loader
from django.shortcuts import render

from .forms import teacherForm, studentForm


def index(request):
    return render(request, "eu/index.html", {})
    #return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return HttpResponse("<h1 style='color:red'>CABELO VERMELHO+99</h1>")

def sobre(request, id):
    names = Student.objects.all()
    template = loader.get_template('eu/sobre.html')
    context = {
        'names': names,
    }
    return render(request, "eu/sobre.html",context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Testando Página %s" % name)

def teacher(request):
    form = teacherForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            send=Teacher.objects.create(name=name)
            send.save()
            return HttpResponse("Data save the in sucess!")
    return render(request, "eu/teacher.html", {"form":form})

def student(request):
    form = studentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            dream = form.cleaned_data["dream"]
            teacher = form.cleaned_data["teacher"]

            teacher_ = Teacher.objects.get(name=teacher)
            send=Student.objects.create(name=name, age=age, dream=dream, teacher=teacher_)
            send.save()
            return HttpResponse("Data save the in sucess!")
    return render(request, "eu/teacher.html", {"form":form})

