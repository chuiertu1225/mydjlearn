from django.urls import path
from App import views
urlpatterns = [
    path('hello/',views.hello),
    path('my/',views.my),
    path('index/',views.index),
    path('home/',views.home),
    path('addstu/',views.addStudent),
]