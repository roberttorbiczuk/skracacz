from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from shortener.forms import WebURLForm
from shortener.models import WebURL
from .base_coder import to_base62


class ShortingURLView(View):

    def get(self, request):
        form = WebURLForm()
        return render(request, 'shortener/index.html', {'form': form})

    def post(self, request):
        form = WebURLForm(request.POST)
        if form.is_valid():
            # Check that url exists in the database
            full_url = form.cleaned_data['full_url']
            weburls = WebURL.objects.filter(full_url=full_url)
            if weburls:
                return HttpResponse(F'Your new URL: {request.get_host()}/{weburls.first().short_url}')
            weburl_instance = form.save()
            weburl_instance.short_url = to_base62(weburl_instance.id)
            weburl_instance.save()
            return HttpResponse(F'Your new URL: {request.get_host()}/{weburl_instance.short_url}')
        return render(request, 'shortener/index.html', {'form': form})


class RedirectFromURLView(View):

    def get(self, request, shorten_url):
        if shorten_url:
            weburl_instance = get_object_or_404(WebURL, short_url=shorten_url)
            return redirect(weburl_instance.full_url)
        else:
            form = WebURLForm()
            return render(request, 'shortener/index.html', {'form': form})

