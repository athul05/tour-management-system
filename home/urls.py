from django.urls import path,include
from . import views

urlpatterns = [path('',views.home,name='home'),
path('join/register',views.register,name='register'),
path ('join/' ,views.join,name='join')
]