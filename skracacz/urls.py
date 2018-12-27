from django.contrib import admin
from django.urls import path
from shortener.views import ShortingURLView, RedirectFromURLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShortingURLView.as_view()),
    path('<str:shorten_url>', RedirectFromURLView.as_view()),
]
