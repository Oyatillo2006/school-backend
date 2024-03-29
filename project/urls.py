from django.contrib import admin
from django.urls import path
from home.views import home, teacher, teacher_edit, teacheredit_after, teacher_del, \
    teacher_add, teacheradd_after, student, student_add, studentadd_after
    # student_edit, studentedit_after





urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("home/", home),
    path("teacher/", teacher),
    path("teacher-edit/<int:d>", teacher_edit),
    path("teacheredit_after/<int:d>/", teacheredit_after),
    path("teacher-del/<int:a>/", teacher_del),
    path("teacher-add/", teacher_add),
    path("teacheradd_after/", teacheradd_after),
    path("student/", student),
    path("student-add/", student_add),
    # path("studentadd_after/", studentadd_after),
    # path("student-edit/<int:id>", student_edit),
    # path("studentedit_after/<int:id>/", studentedit_after),
    # path("student-del/<int:id>/", student),
]
