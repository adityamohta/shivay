from django.contrib import admin

from home.models import Portfolio, Services


class InlineServicesAdmin(admin.TabularInline):
    model = Services


class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ["id", "home_header", "email", "phone"]
    inlines = [InlineServicesAdmin]

    class Meta:
        model = Portfolio


class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "heading"]
    list_display_links = ["id", "heading"]

    class Meta:
        model = Services


admin.site.register(Portfolio, PortfolioModelAdmin)
admin.site.register(Services, ServicesModelAdmin)
