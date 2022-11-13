from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.BankBranchClass, basename='bank')


urlpatterns = [
    path('',views.index),
    path('', include(router.urls)),
]