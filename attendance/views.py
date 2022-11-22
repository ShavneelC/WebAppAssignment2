from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoModelPermissions
from rest_framework.response import Response

from attendance.models import Course, Semester, Lecturer, Student, Classes, CollegeDay
from attendance.permissions import IsAdmin
from attendance.serializer import CourseSerializer, SemesterSerializer, LecturerSerializer, StudentSerializer, \
    ClassesSerializer, CollegeDaySerializer, UserSerializer


# Create your views here.

# Create your views here.

def index(request):
    return HttpResponse("Hello World")


#
# @csrf_exempt
# def course(request):
#     if request.method == "GET":
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = CourseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def course_detail(request, pk):
#     try:
#         course = Course.objects.get(pk=pk)
#     except course.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == "GET":
#         serializer = CourseSerializer(course)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = CourseSerializer(course, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         course.delete()
#         return HttpResponse(status=204)

# Course

@api_view(["GET", "POST"])
def course(request):
    if request.method == "GET":
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = [ DjangoModelPermissions, ]


# Semester

@api_view(["GET", "POST"])
def semester(request):
    if request.method == "GET":
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def semester_detail(request, pk):
    try:
        semester = Semester.objects.get(pk=pk)
    except Semester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SemesterSerializer(semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        semester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]


# Lecturer

@api_view(["GET", "POST"])
def lecturer(request):
    if request.method == "GET":
        lecturer = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturer, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = LecturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def lecturer_detail(request, pk):
    try:
        lecturer = Lecturer.objects.get(pk=pk)
    except Lecturer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LecturerSerializer(semester)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = LecturerSerializer(lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        lecturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]


# Student

@api_view(["GET", "POST"])
def student(request):
    if request.method == "GET":
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]


# Class

@api_view(["GET", "POST"])
def classes(request):
    if request.method == "GET":
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def classes_detail(request, pk):
    try:
        classes = Classes.objects.get(pk=pk)
    except Classes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]


# College Day

@api_view(["GET", "POST"])
def collegeday(request):
    if request.method == "GET":
        collegeday = CollegeDay.objects.all()
        serializer = CollegeDaySerializer(collegeday, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CollegeDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def collegeday_detail(request, pk):
    try:
        collegeday = CollegeDay.objects.get(pk=pk)
    except CollegeDay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CollegeDaySerializer(collegeday)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CollegeDaySerializer(collegeday, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        collegeday.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollegeDayViewSet(viewsets.ModelViewSet):
    queryset = CollegeDay.objects.all()
    serializer_class = CollegeDaySerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]


@api_view(["GET", "POST"])
def users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [DjangoModelPermissions, ]
