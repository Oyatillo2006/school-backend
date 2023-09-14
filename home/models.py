from django.db import models


class School(models.Model):
    number = models.PositiveIntegerField()
    district = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.number} - maktab"


class Subject(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER = (
        ('male', "Male"),
        ('female', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER)
    phone = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    GENDER = (
        ('male', "Male"),
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6,choices=GENDER)
    phone = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
