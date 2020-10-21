from django.contrib import admin
from .models import Destination,Testimonial,Blog,Booking,Enquirie,Feedback
from django.contrib.auth.models import Group
# Register your models here.
from tabular_export.admin import export_to_csv_action, export_to_excel_action
admin.site.unregister(Group)
admin.site.register(Destination)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Feedback)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','place', 'package','date', 'package_prize' ,'number']
    list_display_links= None
    list_per_page=5
    list_filter=['place', 'package']
    search_fields = ['place','package']
    actions=[export_to_excel_action]

admin.site.register(Booking, BookingAdmin)

class EnquirieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','package','number','message']
    list_filter=['package','name']
    list_display_links=None
    list_per_page = 5
    actions=[export_to_excel_action]

admin.site.register(Enquirie,EnquirieAdmin)