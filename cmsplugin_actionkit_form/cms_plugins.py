import cookielib
import urllib
import urllib2


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .models import ActionkitForm


class ActionkitFormPlugin(CMSPluginBase):
    model = ActionkitForm
    name = _("Actionkit Form")
    render_template = "cmsplugin_actionkit_form/form_plugin.html"

    def render(self, context, instance, placeholder):
        try:
            ak_domain = settings.ACTIONKIT_INSTANCE
        except AttributeError:
            context['error'] = 'Actionkit settings not found!'
            return context

        form_url = 'https://{0}/survey/{1}/?abs_urls=1&form_only=1&https_urls=1&download=1'.format(ak_domain, instance.page_name)  # noqa
        form_html = urllib2.urlopen(form_url).read()

        context['actionkit_form'] = form_html
        context['instance'] = instance

        return context

plugin_pool.register_plugin(ActionkitFormPlugin)
