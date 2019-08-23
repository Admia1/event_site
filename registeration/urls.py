from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'registeration'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('user_page/' , views.user_page_view, name="user_page"),
    path('event_group/<int:event_group_pk>/', views.event_group_view, name="event_group"),
    path('event/<int:event_pk>/purchase/', views.purchase_view, name="purchase"),
    path('verify/', views.verify_view, name="verify"),
    path('error/', views.error, name="error"),
    path('api/discount_check/<int:event_group_pk>/', views.discount_check_api, name="discount_check"),
    path('', views.home_view, name="home")
]
