from django.http import HttpResponse
from .models import Student, Teacher
from django.template import loader
from django.shortcuts import render, redirect

from .forms import teacherForm, studentForm, loginForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, "eu/index.html", {})

def login(request):
    try:
        if request.method == "GET":
            return render(request, "eu/login.html", {})
        elif request.method == "POST":
            form = loginForm(request.POST)
            if(form.is_valid()):
                email_ = form.cleaned_data["email"]
                password_ = form.cleaned_data["password"]
                teacher=Teacher.objects.get(email=email_, password=password_)
                return redirect( "main")
            else:
                print("Erro nos dados")
                return render(request, "eu/login.html", {})
    except ObjectDoesNotExist:
        print("Usuário inexistente")
        return render(request, "eu/login.html", {})
    #return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
    if request.method == "GET":
        std=Student.objects.all()
        return render(request, "eu/main.html", {"stds":std})
    elif request.method == "POST":
        print("ERIC")
        std=Student.objects.all()
        return render(request, "eu/main.html", {"stds":std})
    
def register(request):
    if request.method == "GET":
        return render(request, "eu/register.html", {})
    elif request.method == "POST":
        form = teacherForm(request.POST)
        if form.is_valid():
            name_ = form.cleaned_data["name"]
            email_ = form.cleaned_data["email"]
            password_ = form.cleaned_data["password"]
            
            if len(Teacher.objects.filter(email=email_)) == 0:
                teacher=Teacher.objects.create(name=name_, email=email_, password=password_)
                teacher.save()
                return redirect( "login")
            else:
                print("Usuário já cadastrado")
                return render(request, "eu/register.html", {})

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
    if request.method == "GET":
        return render(request, "eu/student.html", {})
    elif request.method == "POST":
        print("PASSO 1  ")
        form = studentForm(request.POST)
        if form.is_valid():
            print("PASSO 2")
            name_ = form.cleaned_data["name"]
            age_ = form.cleaned_data["age"]
            dream_ = form.cleaned_data["dream"]
            class_ = form.cleaned_data["clasS"]
            if len(Student.objects.filter(name=name_, clasS=class_))==0:
                print("PASSO 3")
                teacher_ = Teacher.objects.get(name="rubens")
                std=Student.objects.create(name=name_, age=age_, dream=dream_, clasS=class_, teacher=teacher_)
                std.save()
                #return HttpResponse("Data save the in sucess!")
                return redirect("main")
            else:
                #return HttpResponse("Estudante já cadastrado")
                return render(request, "eu/student.html", {})
    
    elif request.method == "PUT":
        print("")

def student_edit(request, id):
    try:
        print(request.method)
        if request.method == "GET":
            std=Student.objects.get(id=id)
            return render(request, "eu/student_edit.html", {"std":std})
        elif request.method == "POST":
            form = studentForm(request.POST)
            if form.is_valid():
                print("PASSO 2")
                name_ = form.cleaned_data["name"]
                age_ = form.cleaned_data["age"]
                dream_ = form.cleaned_data["dream"]
                class_ = form.cleaned_data["clasS"]

                std=Student.objects.get(name=name_, clasS=class_)
                teacher_ = Teacher.objects.get(name="rubens")

                std.name= name_
                std.age = age_
                std.dream = dream_
                std.clasS = class_
                std.save()
                return redirect("main")
    except ObjectDoesNotExist:
        return redirect("main")
    
    
            
