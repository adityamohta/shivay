from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from home.models import *
from .forms import ContactUsForm


class Home(View):

    def get(self, *args, **kwargs):
        self.request.session["color"] = "brown"
        qs = Event.objects.all().order_by("-organised_on")

        events_qs = qs[:6] if qs.count() > 6 else qs

        gallery_qs = GalleryImage.objects.all()
        context = {
            "events": events_qs,
            "gallery": gallery_qs
        }
        return render(self.request, "home/home.html", context)


def home(request):
    request.session["color"] = "brown"
    qs = Event.objects.all().order_by("-organised_on")
    events_qs = qs[:6] if qs.count() > 6 else qs

    gallery_qs = GalleryImage.objects.all()
    context = {
        "events": events_qs,
        "gallery": gallery_qs
    }
    return render(request, "home/home.html", context)


def events(request):
    request.session["color"] = "brown"
    events_qs = Event.objects.all()
    context = {
        "events": events_qs
    }
    return render(request, "home/events.html", context)


def event_detail(request, pk):
    request.session["color"] = "brown"
    event_obj = get_object_or_404(Event, id=pk)
    context = {
        "event": event_obj
    }
    return render(request, "home/event_detail.html", context)


def about(request):
    request.session["color"] = "brown"
    qs = About.objects.all()
    context = {
        "about_qs": qs
    }
    return render(request, "home/about.html", context)


def contact_us(request):
    request.session["color"] = "brown"
    contact_form = ContactUsForm(request.POST or None)
    if contact_form.is_valid():
        # print(contact_form.cleaned_data)
        contact_form.save(commit=True)
        return redirect('home')
    context = {
        "form": contact_form
    }
    return render(request, "home/contactus.html", context)

