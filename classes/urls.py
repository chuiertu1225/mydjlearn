from django.urls import path
from classes import views

urlpatterns = [
    path('getGrade/',views.getGrade),
    path('getStu/',views.getStu)
]