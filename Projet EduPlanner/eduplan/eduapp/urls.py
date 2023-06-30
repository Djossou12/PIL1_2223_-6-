from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.log , name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser , name='logout'),
    path('',views.index,name='index') ,

    

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='eduapp/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='eduapp/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='eduapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='eduapp/password_reset_complete.html'), name='password_reset_complete'),


     path('Emploisdutempslicence1',views.licence1ep, name='licence1ep'),

    path('Emploisdutempslicence2',views.licence2ep, name='licence2ep'),

    path('Emploisdutempslicence3',views.licence3ep, name='licence3ep'),

    path('Massehorairelicence1',views.massehoraire1, name='massehoraire1'),

    path('Massehorairelicence2',views.massehoraire2, name='massehoraire2'),

    path('Massehorairelicence3',views.massehoraire3, name='massehoraire3'),

    path('IA1',views.IA_1, name='IA_1'),

    path('IA2',views.IA_2, name='IA_2'),

    path('IA3',views.IA_3, name='IA_3'),

    path('IM1',views.IM_1, name='IM_1'),

    path('IM2',views.IM_2, name='IM_2'),

    path('IM3',views.IM_3, name='IM_3'),

    path('GL1',views.GL_1, name='GL_1'),

    path('GL2',views.GL_2, name='GL_2'),

    path('GL3',views.GL_3, name='GL_3'),

    path('SEIoT1',views.SEIoT1, name='SEIoT1'),

    path('SEIoT2',views.SEIoT2, name='SEIoT2'),

    path('SEIoT3',views.SEIoT3, name='SEIoT3'),

    path('SI1',views.SI_1, name='SI_1'),

    path('SI2',views.SI_2, name='SI_2'),

    path('SI3',views.SI_3, name='SI_3'),





]