from django.shortcuts import render, redirect
from .models import Teacher, Subject

def home(request):

    return render(request, "index.html")

def teacher(request):
    if request.POST:
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        subject = request.POST.get("subject")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        teacher = Teacher.objects.get()
        teacher.first_name = f_name
        teacher.last_name = l_name
        teacher.subject = subject
        teacher.phone = phone
        teacher.gender = gender
        return redirect("/teacher/")
    context = {
        "teachers": Teacher.objects.all()
    }
    return render(request, "teacher.html", context)

def teacher_edit(request,d):


    context = {
        "teacher": Teacher.objects.get(id=d),
        "subjects": Subject.objects.all()
    }

    return render(request, "teacher-edit.html", context)

