import random

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def make_shortcode(size=SHORTCODE_MIN, chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = make_shortcode(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return make_shortcode(size=size)
    return new_code
