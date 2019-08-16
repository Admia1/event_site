from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'registeration'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('home/' , views.home_view, name="home"),
    path('event/<int:event_pk>/', views.event_view, name="event"),
    path('event/<int:event_pk>/purchase/', views.purchase_view, name="purchase"),
    path('verify/', views.verify_view, name="verify"),
    path('error/', views.error, name="error"),
    path('', views.show_off_view, name="show_off")
]
