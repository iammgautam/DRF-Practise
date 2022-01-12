from django.db.models import fields
from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        models = Employee
        fields = '__all__'