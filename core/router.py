from app1.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewset)