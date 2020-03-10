from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from Three.models import Student, Grade


def index(request):
    three_index = loader.get_template('three_index.html')
    context = {
        'student_name': 'shark'
    }
    result = three_index.render(context=context)
    print(result)
    # return render(request, 'three_index.html')
    return HttpResponse(result)


def get_grate(request):
    student = Student.objects.get(pk=2)
    grade = student.s_grade
    return HttpResponse('班级是：%s' % grade.g_name)


def get_student(request):
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    context = {
        'students': students
    }
    return render(request, 'student_list_three.html', context=context)







