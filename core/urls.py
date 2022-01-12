
from django.contrib import admin
from .router import router
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('/api', include('api.urls')),
]
