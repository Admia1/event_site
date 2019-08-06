from django.urls import path
from . import views

app_name = 'registeration'

urlpatterns = [
    path('hello_world/', views.hello_world, nane="hello"),
]
