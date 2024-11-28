from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('loginn/', views.loginn,name='loginn'),
    path('signup/', views.signup,name='signup'),
    path('home/', views.home,name='home'),
    
]
