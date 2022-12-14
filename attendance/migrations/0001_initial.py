# Generated by Django 4.1.3 on 2022-11-21 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_number', models.IntegerField(default='0', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('dob', models.DateField(default='1998-01-01')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('staff_id', models.IntegerField(default='0', primary_key=True, serialize=False)),
                ('dob', models.DateField(default='1998-01-01')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('semester', models.ManyToManyField(to='attendance.semester')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeDay',
            fields=[
                ('date', models.DateField(default='1998-01-01', primary_key=True, serialize=False)),
                ('classes', models.ManyToManyField(to='attendance.classes')),
                ('student', models.ManyToManyField(to='attendance.student')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.course'),
        ),
        migrations.AddField(
            model_name='classes',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.lecturer'),
        ),
        migrations.AddField(
            model_name='classes',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.semester'),
        ),
        migrations.AddField(
            model_name='classes',
            name='student',
            field=models.ManyToManyField(to='attendance.student'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default='True')),
                ('marked', models.BooleanField(default='False')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.classes')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.collegeday')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.student')),
            ],
        ),
    ]
