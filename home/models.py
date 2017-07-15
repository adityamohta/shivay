from __future__ import unicode_literals

from django.db import models


class Portfolio(models.Model):
    # Home
    home_image = models.ImageField(upload_to="home/", blank=True, null=True)
    home_header = models.CharField(max_length=255, default="MAKE YOUR DREAM EVENT A REALITY")
    home_text = models.TextField(null=True, blank=True)
    # About
    about_header = models.CharField(max_length=255, default="We've got what you need!")
    about_text = models.TextField(null=True, blank=True)
    # Contact us
    contact_text = models.TextField(
        default="""
                Ready to start your next project with us? That's great! 
                Give us a call or send us an email and we will get back to you as soon as possible!
            """
    )
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25)


class Events(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    title = models.CharField(max_length=255, default="Kota, Rajasthan")
    category = models.CharField(max_length=255, default="Venue")
    thumbnail = models.ImageField(
        upload_to="events/thumbs/",
        help_text="Width not more then 650 px",
        null=True
    )
    image = models.ImageField(
        upload_to="events/",
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


class Services(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    image = models.ImageField(upload_to="services/")
    heading = models.CharField(max_length=255)
    text = models.TextField()
