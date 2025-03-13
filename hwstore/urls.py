from django.urls import path
from . import views

app_name = 'burger_shop'

urlpatterns = [
    path('', views.index, name='homepage'),

]