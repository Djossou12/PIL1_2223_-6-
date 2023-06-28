from django.urls import path
from . import views

app_name = "eduapp"
urlpatterns = [
    path('login/', views.log , name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser , name='logout'),
    path('',views.index,name='index') ,
   
]