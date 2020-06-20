from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ImageViewSet 
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
#router.register('users',UserViewSet)
router.register(r'image',ImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
