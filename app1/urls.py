from app1 import views
from django.urls import path , include

urlpatterns = [
    
     path('home/', views.home , name= 'home'),
     path('', views.signuppage , name= 'signup'),
     path('login/', views.loginpage , name= 'login'),
     path('logout/', views.logoutpage , name= 'logout'),

]