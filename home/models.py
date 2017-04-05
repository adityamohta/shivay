from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class WebsiteTheme(models.Model):
    color = models.CharField(max_length=255, default="brown")

    def __unicode__(self):
        return self.color


class About(models.Model):
    text = models.TextField(null=True, blank=True)


class ContactUs(models.Model):
    text = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.phone_number


class EventImage(models.Model):
    image = models.ImageField(upload_to="events/", null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    event = models.ForeignKey("Event", null=True, blank=True, related_name="images")


class EventVideo(models.Model):
    url = models.CharField(max_length=1000)
    event = models.ForeignKey("Event", null=True, blank=True, related_name="videos")


class Event(models.Model):
    title = models.CharField(max_length=255)
    organised_on = models.DateTimeField()
    text = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.id})


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/",  null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)


class HomeScreenDetail(models.Model):
    url = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="home_screen/", null=True, blank=True)
    title = models.CharField(max_length=255)
