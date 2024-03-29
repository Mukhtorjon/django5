from  django import forms
from django.forms import ModelForm
from .models import Venue,Event
class EventFormAdmin(ModelForm):
    class Meta:
        model=Event
        fields=('name','event_data','venue','attendees','description')
        labels={
            'name':'',
            'event_data':'',
            'venue':'Venue',
            'attendees':'Attendees',
            'description':'',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'event_data':forms.TextInput(attrs={'class':'form-control','placeholder':'Event date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
            
        }
        
        
class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=('name','event_data','venue','manager','attendees','description')
        labels={
            'name':'',
            'event_data':'',
            'venue':'Venue',
            'manager':'Manager',
            'attendees':'Attendees',
            'description':'',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'event_data':forms.TextInput(attrs={'class':'form-control','placeholder':'Event date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
            
        }
        
        
class VenueForm(ModelForm):
    class Meta:
        model=Venue
        fields=('name','address','zip_code','phone','web','email_address','venue_image')
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
            'venue_image':'',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})
            
        }