from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView),
    path(r'login/',views.User_Login,name = 'Login'),
    path(r'register/', views.User_Register, name='Register'),
]
