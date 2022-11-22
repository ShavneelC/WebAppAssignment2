from django.contrib import admin
from django.contrib.auth.models import User

from attendance.models import Student, Lecturer, Classes, Course, Semester, CollegeDay, Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(CollegeDay)
admin.site.register(Attendance)