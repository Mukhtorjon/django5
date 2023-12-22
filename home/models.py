from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Venue(models.Model):
    name=models.CharField('Venue Name',max_length=120)
    address=models.CharField(max_length=300)
    zip_code=models.CharField('Zip Code',max_length=100)
    phone=models.CharField('Contact Phone',max_length=100,blank=True)
    web=models.URLField('Website Address',blank=True)
    email_address=models.EmailField('Email',blank=True)
    owner=models.IntegerField('Venue Owner',blank=False,default=1)
    venue_image=models.ImageField(null=True,blank=True,upload_to="venue_image/")
    def __str__(self):
        return self.name
class MyClubUser(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField('User Email')
    def __str__(self):
        return self.firstname + " " + self.lastname
class Event(models.Model):
    name=models.CharField("Event Name",max_length=120)
    event_data=models.DateTimeField('Event Data')
    # venue=models.CharField(max_length=100)
    venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    # manager=models.CharField(max_length=60)
    manager=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description=models.TextField(blank=True)
    attendees=models.ManyToManyField(MyClubUser,blank=True)
    def __str__(self):
        return self.name