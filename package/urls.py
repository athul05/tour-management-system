from django.urls import path
from . import views

urlpatterns = [path('',views.usr_indx,name='home'),
path('package_details/',views.pkg_details,name='package_details'),
path('packages/',views.pkgs,name='packages'),
path('testimonial/',views.testim,name='testimonial'),
path('about/',views.about,name='about'),
path ('checkout/',views.checkout,name='checkout')
]