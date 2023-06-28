from django.contrib import admin
from django.urls import re_path
from shortener.views import kirr_redirect_view, KirrCBView

urlpatterns = [
    re_path(r'^new-admin/', admin.site.urls),
    re_path(r'^view-1/$', kirr_redirect_view),
    re_path(r'^view-2/$', KirrCBView.as_view),
]
