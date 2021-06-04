from django.contrib import admin
from .models import complaint


admin.site.site_header = "Complaint Admin"
admin.site.site_title = "Complaint Admin Portal"
admin.site.index_title = "Welcome to Complaint admin Portal"

def Mark_Done(modeladmin, request, queryset):
    queryset.update(Status='Done')

def Mark_Working(modeladmin, request, queryset):
    queryset.update(Status='Working')

Mark_Done.short_description = "Mark as Done"
Mark_Working.short_description = "Mark as Working"

class FormAdmin(admin.ModelAdmin):
    list_display=['Complain_id', 'Name','Assigned_Date', 'Completed_Date', 'Description', 'Status']
    list_filter=['Status','Assigned_Date', 'Completed_Date']
    actions=[Mark_Done, Mark_Working]
    search_fields=['Complain_id', 'Name']

admin.site.register(complaint, FormAdmin)
