from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Portfolio(models.Model):
    # Home
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


class Services(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    image = models.ImageField(upload_to="services/")
    heading = models.CharField(max_length=255)
    text = models.TextField()
