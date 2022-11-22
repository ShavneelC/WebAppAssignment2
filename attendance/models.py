from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.IntegerField(primary_key=True, default='0')
    dob = models.DateField(default='1998-01-01')

    @property
    def full_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return str(self.full_name)


class Semester(models.Model):
    semester_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    semester = models.IntegerField()

    @property
    def full_semester(self):
        return '%s %s' % (self.semester, self.year)

    def __str__(self):
        return self.full_semester


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(primary_key=True, max_length=200)
    dob = models.DateField(default='1998-01-01')

    @property
    def student_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return str(self.student_name)


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    semester = models.ManyToManyField(Semester)

    def __str__(self):
        return self.name


class Classes(models.Model):
    class_number = models.IntegerField(primary_key=True, default='0')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.course)


class CollegeDay(models.Model):
    date = models.DateField(primary_key=True, default='1998-01-01')
    classes = models.ManyToManyField(Classes)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.date)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.ForeignKey(CollegeDay, on_delete=models.CASCADE)
    status = models.BooleanField(default='True')
    marked = models.BooleanField(default='False')

    @property
    def attendancedetail(self):
        return '%s   |   %s | %s %s' % (
        self.date.date, self.classes.course.name, self.student.user.first_name, self.student.user.last_name)

    def __str__(self):
        return str(self.attendancedetail)