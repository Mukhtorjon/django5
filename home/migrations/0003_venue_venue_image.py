# Generated by Django 4.2.2 on 2023-12-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/venue_image/'),
        ),
    ]
