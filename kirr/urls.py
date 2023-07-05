from django.contrib import admin
from django.urls import re_path
from shortener.views import kirr_redirect_view, KirrCBView, test_view
from shortener import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^(?P<shortcode>[\w-]+){6, 15}/$', kirr_redirect_view),
    re_path(r'^b/(?P<shortcode>[\w-]+){6, 15}/$', KirrCBView.as_view()),
    re_path(r'^about123/$', test_view),
]
