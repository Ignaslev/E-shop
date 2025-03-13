from django.urls import path
from . import views

app_name = 'hwstore'

urlpatterns = [
    path('', views.index, name='homepage'),

]