from django.contrib import admin
from django.urls import path
from home.views import home, teacher, teacher_edit




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("home/", home),
    path("teacher/", teacher),
    path("teacher-edit/<int:d>", teacher_edit),
]
