from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from asset.models import Asset
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'This checks if there are any expired assets and email the admin about it'

    def handle(self, *args, **options):
        self.stdout.write("Checking assets")
        try:
            assets = Asset.objects.filter(valid_until__lte=datetime.now()+timedelta(days=31))
        except ObjectDoesNotExist:
            pass

        if assets:
            asset_names = []
            self.stdout.write(str(len(assets)) + " assets found")

            for asset in assets:
                asset_names.append(asset.title)

                #send mail here
