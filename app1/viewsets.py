from rest_framework import viewsets
from .models import Users
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = serializers.UserSerializers