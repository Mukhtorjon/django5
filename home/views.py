from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event,Venue
from .form import VenueForm,EventForm,EventFormAdmin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from django.contrib import messages
# Generate Pdf File Venue List
def venue_pdf(request):
    venues=Venue.objects.all()
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    lines=[]
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append('')
    # lines=['This is line 1\n','This is line 2\n','This is line 3\n']
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='venue.pdf')



def venue_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename=venues.csv'
    writer=csv.writer(response)
    venues=Venue.objects.all()
    
    writer.writerow(['Venue Name','Address','Zip Code','Phone','Web Address','Email'])
    
    # lines=['This is line 1\n','This is line 2\n','This is line 3\n']
    lines=[]
    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.phone,venue.web,venue.email_address])
        
    response.writelines(lines)
    return response

def venue_txt(request):
    response=HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment;filename=venues.txt'
    writer=csv.writer(response)
    venues=Venue.objects.all()
    # lines=['This is line 1\n','This is line 2\n','This is line 3\n']
    lines=[]
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n')

    response.writelines(lines)
    return response




# Create your views here.
def add_event(request):
    submitted=False
    if request.method=="POST":
        if request.user.is_superuser:
            form=EventForm(request.POST)
            if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/add_event?submitted=True")
        else:
            form=EventForm(request.POST)
            if form.is_valid():
                event=form.save(commit=False)
                event.owner=request.user
                event.save()
                return HttpResponseRedirect("/add_event?submitted=True")
    else:
        # Just going to the page not submitting
        if request.user.is_superuser:
              form=EventForm
        else:
            form=EventFormAdmin
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'add_event.html', {'form':form,'submitted':submitted})

def update_event(request, event_id):
    event=Event.objects.get(pk=event_id)
    if request.user.is_superuser:
         form=EventFormAdmin(request.POST or None, instance=event)
    else:
        form=EventForm(request.POST or None,instance=event)
    if form.is_valid():
        form.save()
        return redirect("events_list")
    return render(request,'update_event.html',{'event':event,'form':form} )

def delete_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    if request.user==event.manager:
        event.delete()
        messages.success(request,('Event Delated!!'))
        return redirect("events_list")
    else:
        messages.success(request,("You aren't Authorized To Delete This Event!"))
        return redirect("events_list")

def update_venue(request, venue_id):
    venue=Venue.objects.get(pk=venue_id)
    form=VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect("list_venue")
    return render(request,'update_venue.html',{'venue':venue,'form':form} )

def delete_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect("list_venue")
    
def search_venue(request):
    if request.method=="POST":
        searched=request.POST['searched']
        venues=Venue.objects.filter(name__contains=searched)
        
        return render(request,'search.html',{'searched':searched,'venues':venues})
    else:
        return render(request,'search.html',{})


def show_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    return render(request,'show_venue.html',{'venue':venue} )


def list_venues(request):
    # venue_list=Venue.objects.all().order_by('?')
    venue_list=Venue.objects.all()
    p=Paginator(Venue.objects.all(),3)
    page=request.GET.get('page')
    venues=p.get_page(page)
    nums= "a" * venues.paginator.num_pages
    return render(request,'venue.html',{'venue_list':venue_list,'venues':venues,'nums':nums})


def add_venue(request):
    submitted=False
    if request.method=="POST":
         form=VenueForm(request.POST)
         if form.is_valid():
             venue=form.save(commit=False)
             venue.owner=request.user.id
             venue.save()
             return HttpResponseRedirect("/venue?submitted=True")
    else:
        form=VenueForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'add_venue.html', {'form':form,'submitted':submitted})


def all_event(request):
    event_list=Event.objects.all().order_by('name')
    return render(request, 'events_list.html', {'event_list':event_list})
   
    
def home (request,year=datetime.now().year, month=datetime.now().strftime('%B')):
    name='Jhon'
    month=month.title()
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)
    cal=HTMLCalendar().formatmonth(year,month_number)
    now=datetime.now()
    current_year=now.year
    time=now.strftime('%I:%M:%p')
    return render(request,'home.html',
                  {'name':name,
                   'cal':cal,
                   'current_year':current_year,
                   'time':time
                   })