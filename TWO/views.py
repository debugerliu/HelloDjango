import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from TWO.models import Student


def index(request):
    return HttpResponse(123666)


def add_student(request):
    student = Student()
    student.s_name = 'Tom%d' % random.randrange(100)
    student.s_age = random.randrange(100)
    student.save()
    return HttpResponse('添加成功 %s' % student.s_name)


def get_student(request):
    students = Student.objects.all()
    for i in students:
        print(i)

    # return HttpResponse('查询成功')
    context = {
        'hobby': 'game',
        'eat': 'meat',
        'students': students
    }
    return render(request, 'student_list.html', context=context)


def update_student(request):
    student = Student.objects.get(pk=3)
    student.s_name = 'Tom000'
    student.save()
    return HttpResponse('更新成功')


def delete_student(request):
    student = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse('删除成功')
