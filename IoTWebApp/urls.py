from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('signout/', views.SignOut, name='signout'),
    path('signin/', views.SignIn,name='signin'),
]