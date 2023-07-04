from django.contrib import admin
from django.urls import re_path
from shortener.views import kirr_redirect_view, KirrCBView
from shortener import views

urlpatterns = [
    re_path(r'^new-admin/', admin.site.urls),
    re_path(r'^a/(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    re_path(r'^b/(?P<shortcode>[\w-]+)/$', KirrCBView.as_view()),
]
