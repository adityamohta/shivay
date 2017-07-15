from django.http import JsonResponse
from django.shortcuts import render, Http404
from django.views.generic import View

from home.models import Portfolio, Services


class ServiceDetailAPIView(View):

    def get_object(self, pk):
        try:
            obj = Services.objects.get(id=pk)
            return obj
        except:
            raise Http404

    def get(self, *args, **kwargs):
        if self.request.is_ajax():
            obj = self.get_object(kwargs["pk"])
            response = {
                "id": obj.id,
                "text": obj.text
            }
            return JsonResponse(response, status=201)
        raise Http404


class Home(View):

    def get_object(self):
        qs = Portfolio.objects.all()
        if qs.exists():
            return qs.first()
        raise Http404

    def get(self, *args, **kwargs):
        obj = self.get_object()
        context = dict(
            home_header=obj.home_header,
            home_text=obj.home_text,
            about_header=obj.about_header,
            about_text=obj.about_text,
            contact_text=obj.contact_text,
            email=obj.email,
            phone=obj.phone,
            services=obj.services_set.all()
        )
        return render(self.request, "index.html", context)
