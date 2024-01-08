from django.contrib import admin
from .models import Venue,Event,MyClubUser



admin.site.register (MyClubUser)
@admin.register (Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=('name','address','phone')
    ordering=('name',)
    search_fields=('name','address')
    
    
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(('name',  'venue'),'event_data','description','manager','aprroved')
    list_display=('name','event_data','venue','manager')
    list_filter=('event_data','venue')
    ordering=('-event_data',)