from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(
        School, related_name="classrooms", on_delete=models.CASCADE
    )
    year_level = models.PositiveSmallIntegerField()
    room_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.school.abbreviation} {self.year_level}/{self.room_number}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    classrooms = models.ManyToManyField(Classroom, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    classroom = models.ForeignKey(
        Classroom, related_name="students", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
