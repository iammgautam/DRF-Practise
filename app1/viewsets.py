from rest_framework import viewsets
from .models import Employee
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializers