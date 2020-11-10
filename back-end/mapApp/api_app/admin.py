
from django.contrib import admin
from .models import Coordinates
from .models import ItsmIncidents
from .models import Comments
# Register your models here.


@admin.register(ItsmIncidents)
class itsm(admin.ModelAdmin):
    list_display = ('id','platform_inc_number','site_id' ,'status_inc','inc_description' , 'priority_incident', 'traffic_affected')
    ordering = ('traffic_affected',)
    search_fields = ('platform_inc_number', 'site_id', 'status_inc')

@admin.register(Coordinates)
class itsm(admin.ModelAdmin):
    list_display = ('site_name','town' ,'region' , 'address', 'long_id', 'lat_id')

    search_fields = ('site_name','town' ,'region' , 'address')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new','text' ,'created', 'moderation')

admin.site.register(Comments, CommentAdmin)
# admin.site.register(ItsmIncidents)


