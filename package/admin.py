from django.contrib import admin
from .models import Destination,Testimonial,Blog,Booking,Enquirie,Feedback
from django.contrib.auth.models import Group
# Register your models here.
from tabular_export.admin import export_to_csv_action, export_to_excel_action
admin.site.unregister(Group)
admin.site.register(Destination)
admin.site.register(Testimonial)
admin.site.register(Blog)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'name', 'subject', 'message', 'rating')
    list_filter = ('username','rating')
    list_display_links=None
    list_per_page=5
    actions=[export_to_excel_action]

admin.site.register(Feedback, FeedbackAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['username','id', 'name','place', 'package','date', 'package_prize' ,'number']
    list_display_links= None
    list_per_page=5
    list_filter=['place', 'package','username']
    search_fields = ['place','package']
    actions=[export_to_excel_action]

admin.site.register(Booking, BookingAdmin)

class EnquirieAdmin(admin.ModelAdmin):
    list_display = [ 'username' ,'id', 'name','package','number','message','urgent']
    list_filter=['package','username','urgent']
    list_display_links=None
    list_per_page = 5
    actions=[export_to_excel_action]

admin.site.register(Enquirie,EnquirieAdmin)