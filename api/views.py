from typing import Counter
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer, JSONResponse
from django.http import HttpResponse

# Create your views here.
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    json_data =JSONRenderer().render(serializer)
    # print(json_data)

    return HttpResponse(json_data, content_type = 'application/json')

def student_detail(request, id):
    stu = Student.objects.get(pk = id)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer)

    return HttpResponse(json_data, content_type = 'application/json')
