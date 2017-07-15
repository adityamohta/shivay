from django.contrib import admin

from home.models import Events, Portfolio, Services


class InlineServicesAdmin(admin.TabularInline):
    model = Services
    extra = 1


class InlineEventsAdmin(admin.TabularInline):
    model = Events
    extra = 1


class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ["id", "home_header", "email", "phone"]
    list_display_links = ["id", "home_header"]
    inlines = [InlineServicesAdmin, InlineEventsAdmin]

    class Meta:
        model = Portfolio


class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "heading"]
    list_display_links = ["id", "heading"]

    class Meta:
        model = Services


class EventsModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

    class Meta:
        model = Events


admin.site.register(Portfolio, PortfolioModelAdmin)
admin.site.register(Services, ServicesModelAdmin)
admin.site.register(Events, EventsModelAdmin)
