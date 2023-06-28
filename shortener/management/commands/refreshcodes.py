from django.core.management.base import BaseCommand

from kirr.shortener.models import KirrURL


class Command(BaseCommand):
    help = "Refreshes all KirrURL shortcodes"

    def add_arguments(self, parser):
        parser.add_argument("poll_ids", type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
