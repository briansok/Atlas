from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import get_object_or_404
from info.models import Notification
from asset.models import Asset
from location.models import Section

class CreateNotification(object):

    def __init__(self, title, notification_type, request, asset=None, section=None):
        self.title = title
        self.notification_type = notification_type
        self.request = request
        self.user = request.user
        self.asset = asset
        self.section = section

    def create(self):
        if self.asset:
            self.asset = get_object_or_404(Asset, id=self.asset)

        if self.section:
            self.section = get_object_or_404(Section, id=self.section)

        Notification.objects.create(
            title=self.title,
            notification_type=self.notification_type,
            asset=self.asset,
            section=self.section,
            created_by=self.user
        )

        messages.add_message(self.request, messages.INFO, self.title)


