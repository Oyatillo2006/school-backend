from django.shortcuts import render, redirect
from .models import Teacher, Subject, Student

def home(request):

    return render(request, "index.html")

def teacher(request):
    context = {
        "teachers": list(Teacher.objects.all()),
    }

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


def student(request):
        context = {
            "students": list(Student.objects.all()),
        }

        return render(request, "student.html", context)

def student_add(request):

    return render(request, "student_add.html")


def studentadd_after(request):
    if request.POST:
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        grade = request.POST.get("grade")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        Student.objects.create(first_name=f_name, last_name=l_name, grade=grade, phone=phone, age=age,
                               gender=gender)

        return redirect("/student/")

def student(request,id):
    context = {
        "student": Teacher.objects.get(id=id),
    }

    return render(request, "student-edit.html", context)
