from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ActionkitForm(CMSPlugin):
    """
    Configuration data for an Actionkit Form CMSPlugin.
    """
    page_name = models.CharField(max_length=255)

    def __str__(self):
        return _("CMS Plugin for {0}".format(self.page_name))
