from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'registeration'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('home/' , views.home_view, name="home"),
    path('purchase/<int:event_pk>/', views.purchase_view, name="purchase"),
    path('verify/', views.verify_view, name="verify"),
    path('error/', views.error, name="error"),
    path('', views.show_off_view, name="show_off")
]
