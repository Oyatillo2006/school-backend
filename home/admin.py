from django.contrib import admin

from .models import Student, Subject, Teacher

admin.site.register([Student,Subject,Teacher])