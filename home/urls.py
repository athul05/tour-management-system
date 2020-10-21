from django.urls import path,include
from . import views

urlpatterns = [path('',views.home,name='home'),
path('about/', views.about, name='about'),
path('contact/',views.contact, name='contact'),
path('about/contact', views.abcontact, name ='contact'),
path('join/register',views.register,name='register'),
path('join/login',views.login, name='login'),
path ('join/' ,views.join,name='join'), 
path('join/signin', views.signin, name='signin')
]