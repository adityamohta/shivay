from django.contrib import admin

from home.models import *


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["text", "phone_number", "email", "timestamp"]

    class Meta:
        model = ContactUs


class InlineEventImageAdmin(admin.TabularInline):
    model = EventImage


class InlineEventVideoAdmin(admin.TabularInline):
    model = EventVideo


class EventModelAdmin(admin.ModelAdmin):

    inlines = [
        InlineEventImageAdmin,
        InlineEventVideoAdmin
    ]

    class Meta:
        model = Event


admin.site.register(WebsiteTheme)
admin.site.register(About)
admin.site.register(ContactUs, ContactModelAdmin)
admin.site.register(EventImage)
admin.site.register(EventVideo)
admin.site.register(Event, EventModelAdmin)
admin.site.register(GalleryImage)
admin.site.register(HomeScreenDetail)
