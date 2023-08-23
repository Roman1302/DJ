from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.address, name='my'),
    path('activity/', views.activity, name='activity'),
]