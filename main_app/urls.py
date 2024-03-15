from django.urls import path
from .views import *
urlpatterns=[
    path('',setsession,name='setsession'),
    path('dels/',delsession,name='delsession'),
    path('gets/',getsession,name='getsession'),
]