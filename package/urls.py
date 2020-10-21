from django.urls import path
from . import views

urlpatterns = [path('usr/',views.usr,name='usr'),
path('usr/feedback',views.feedback,name='feedback'),
path('usr/packages/index',views.index,name='index'),
path('usr/contact/index',views.index,name='index'),
path('usr/about/index',views.index,name='index'),
path('usr/packages/package_details/index/',views.index,name='index'),
path('usr/package_details/index/',views.index,name='index'),
path('usr/package_details/<int:oid>',views.pkg_details,name='package_details'),
path('usr/packages/',views.pkgs,name='packages'),
path('usr/packages/package_details',views.pkg_details,name='packages'),
path('usr/about/',views.about,name='about'),
path('usr/packages/about/',views.about,name='about'),
path('usr/package_details/about/',views.about,name='about'),
path('usr/packages/package_details/about/',views.about,name='about'),
path('usr/package_details/enquiry/<int:oid>',views.enquiry,name='enquiry'),
path('usr/contact/',views.contact,name='contact'),
path('usr/packages/contact/',views.contact,name='contact'),
path('usr/package_details/contact/',views.contact,name='contact'),
path('usr/packages/package_details/contact/',views.contact,name='contact'),
path ('usr/package_details/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/package_details/checkout/usr',views.sucess,name='success'),
path ('usr/packages/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/package_details/checkout/<int:oid>',views.checkout,name='checkout'),
path ('usr/packages/package_details/checkout/pay',views.checkout,name='checkout'),
path ('usr/logout', views.logout,name='checkout')
]