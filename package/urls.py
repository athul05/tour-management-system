from django.urls import path
from . import views

urlpatterns = [path('usr/',views.usr,name='usr'),
path('usr/package_details/<int:oid>',views.pkg_details,name='package_details'),
path('usr/packages/',views.pkgs,name='packages'),
path('usr/packages/package_details',views.pkg_details,name='packages'),
path('usr/testimonial/',views.testim,name='testimonial'),
path('usr/about/',views.about,name='about'),
path ('usr/package_details/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/package_details/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/package_details/checkout/pay',views.checkout,name='checkout'),
path ('usr/logout', views.logout,name='checkout')
]