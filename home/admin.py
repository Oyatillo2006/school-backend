from django.contrib import admin

from .models import School, Student, Subject, Teacher

admin.site.register([School,Student,Subject,Teacher])