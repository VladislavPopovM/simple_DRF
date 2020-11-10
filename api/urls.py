from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import InvestorViewSet, PassportViewSet, QualificationViewSet

router = routers.DefaultRouter()
router.register('investors',InvestorViewSet)
router.register('passports',PassportViewSet)
router.register('qualification',QualificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]