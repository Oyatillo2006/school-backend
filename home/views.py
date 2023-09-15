from django.shortcuts import render, redirect
from .models import Teacher, Subject

def home(request):

    return render(request, "index.html")

def teacher(request):
    context = {
        "teachers": list(Teacher.objects.all()),
        "len": len(Teacher.objects.all()),
        "num":[]
    }

    date = {
        "info": {}
    }

    for i in range(1, context["len"]+1):
        context["num"].append(i)
    print(context["teachers"])
    print(context["num"])

    for i in range(context["len"]):
        date["info"].update({context["num"][i] : context["teachers"][i]})
    print(date["info"])

    return render(request, "teacher.html", context)


def teacher_add(request):
    context = {
        "subjects": Subject.objects.all()
    }

    return render(request, "teacher_add.html", context)

def teacheradd_after(request):
    if request.POST:
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        name = request.POST.get("subject")
        subject = Subject.objects.get(name=name)
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        Teacher.objects.create(first_name = f_name, last_name = l_name, subject = subject, phone = phone,age = age, gender = gender)

        return redirect("/teacher/")

def teacher_edit(request,d):
    context = {
        "teacher": Teacher.objects.get(id=d),
        "subjects": Subject.objects.all()
    }

    return render(request, "teacher-edit.html", context)

def teacher_del(request, a):
    Teacher.objects.get(id=a).delete()

    return redirect("/teacher/")

def teacheredit_after(request,d):
    if request.POST:
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        subject = request.POST.get("subject")
        s = Subject.objects.get(name=subject)
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        teacher = Teacher.objects.get(id=d)
        teacher.first_name = f_name
        teacher.last_name = l_name
        teacher.subject = s
        teacher.phone = phone
        teacher.age = age
        teacher.gender = gender
        teacher.save()
        return redirect("/teacher/")
