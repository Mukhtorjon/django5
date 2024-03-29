from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>/',views.home,name='home'),
    path('event',views.all_event,name='events_list'),
    path('venue',views.add_venue,name='add_venue'),
    path('list_venue',views.list_venues,name='list_venue'),
    path('show_venue/<venue_id>',views.show_venue,name='show_venue'),
    path('search_event',views.search_event,name='search_event'),
    path('search',views.search_venue,name='search'),
    path('update_venue/<venue_id>',views.update_venue,name='update_venue'),
    path('delete_venue/<venue_id>',views.delete_venue,name='delete_venue'),
    path('update_event/<event_id>',views.update_event,name='update_event'),
    path('delete_event/<event_id>',views.delete_event,name='delete_event'),
    path('add_event',views.add_event,name='add_event'),
    path('venue_csv',views.venue_csv,name='venue_csv'),
    path('venue_pdf',views.venue_pdf,name='venue_pdf'),
    path('venue_txt',views.venue_txt,name='venue_txt'),
    path('my_event',views.my_event,name='my_event'),
    path('admin_aprroval',views.admin_aprroved,name='admin_aprroval'),
    path('venue_events/<venue_id>',views.venue_event,name='venue_events'),
    path('show_event/<event_id>',views.show_events,name='show_event'),

]