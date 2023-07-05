from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import KirrURL


# Create your views here.

def test_view():
    return HttpResponse("some stuff")


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse(obj.url)


class KirrCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse(f"hello again {shortcode}".format(shortcode=shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()


'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    print(request.method)

    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # obj_url = obj.url

    # NOT RECOMMENDED
    #
    # try:
    #     obj = KirrURL.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()
    #
    # NOT RECOMMENDED

    # obj = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    return HttpResponse(f"hello {shortcode}".format(shortcode=obj.url))
'''
