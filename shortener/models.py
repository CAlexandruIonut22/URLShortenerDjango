from django.db import models
import random


def make_shortcode(size=6, chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'):
    return ''.join(random.choice(chars) for _ in range(size))


class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=8, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    test = models.CharField(max_length=3)

    def save(self, *args, **kwargs):
        print(self)
        self.shortcode = make_shortcode()
        super(KirrURL, self).save(*args, **kwargs)

    # def my_save(self, *args, **kwargs):
    #     self.save()

    # empty_datetime = models.DateTimeField(auto_now=False)
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


# Create your models here.


'''
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
'''
