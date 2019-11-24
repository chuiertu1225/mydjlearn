from django.shortcuts import render
from django.http.response import HttpResponse
from classes.models import Student,Grade
# Create your views here.
def getGrade(request):
    student = Student.objects.get(pk = 3)
    grade = student.grade
    return HttpResponse('获取成功 %s' % grade.name)

def getStu(request):
    grade = Grade.objects.get(pk = 1)
    students = grade.student_set.all()
    print(students)
    return HttpResponse('获取成功')