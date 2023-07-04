from django.http import HttpResponse
from django.views import View


# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    print(shortcode)
    return HttpResponse(f"hello {shortcode}".format(shortcode=shortcode))


class KirrCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)

        return HttpResponse(f"hello again {shortcode}".format(shortcode=shortcode))
