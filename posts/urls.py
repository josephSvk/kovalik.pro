from django.urls import path
from . import views


urlpatterns = [
     path("testfoto/", views.testfoto, name='testfoto'),
]